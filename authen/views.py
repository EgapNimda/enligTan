from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import myuser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Plase try some either")
            return redirect('signin')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist! Plase try some either")
            return redirect('signin')
        
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
        if password!=conpassword:
            messages.error(request,"Passwords didn't match")
        if not  username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('signin')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=username
        myuser.save()

    return render(request,"signUp.html")

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username)
            password_valid = user.check_password(password)
            if password_valid:
                pass
            else:
                messages.error(request,"Bad Credentials")
                return redirect('home')

            if user is not None:
                user = authenticate(username=user.username, password=password)
                login(request,user)
                return render(request,"main.html")
            else:
                return redirect('singIn')

        except:
            messages.error(request, "Bad")
            return redirect('signIn')
    return render(request, 'main.html')
