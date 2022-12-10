from django.shortcuts import render

def account (request):
    return render(request, "signIn.html")


def signin (request):
    return render(request,"signIn.html")


def signup (request):
    return render(request, "signUp.html")
