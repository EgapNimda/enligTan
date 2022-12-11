from django.shortcuts import render
from django.http import HttpResponse
from .models import myuser


def signIn(request):
    # description = myuser.objects.
    return render(request,"signIn.html")

def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if(conpassword == password) :
            for i in range(0,10):
                print("meow")
    return render(request,"signUp.html")
