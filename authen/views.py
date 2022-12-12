from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import myuser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

User = get_user_model()


def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['mail']
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
        return render(request,"main.html")

    return render(request,"signUp.html")

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if(User.objects.filter(username=username)):
            user = User.objects.get(username=username)
            password_valid = user.check_password(password)

            if password_valid :
                if user is not None:
                    user = authenticate(username=user.username, password=password)
                    login(request,user)
                    return render(request,"main.html")
                else:
                    return redirect('signIn')
            else:
                messages.error(request, "Bad")
                return redirect('signIn')
                
        
        else:
            messages.error(request, "Bad")
            return redirect('signIn')

    return render(request, 'signIn.html')


def signOut(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return render(request,"main.html")

def changeProfile(request):
    if request.method == 'POST':
        newusername = request.POST['username']
        newemail = request.POST['email']
        print(request.user.username)
        use = User.objects.get(username=request.user.username)
        use.update(username=newusername)
        use.update(email=newemail)
    return redirect('signIn')

def viewProfile(request):
  
    return render(request, "viewProfile.html")