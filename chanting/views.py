
from django.http import HttpResponse
from django.template import loader
from chanting.time import monk_day
from django.shortcuts import render

def main(request):

    if monk_day():
        s = "วันนี้วันพระ"
    
    else:
        s = ""
    context = {
        "monk" : s
    }
    return render(request,"main.html",context)

def viewProfile(request):
  
    return render(request, "viewProfile.html")

def suadPrajum(request):
    return render(request, "suadPrajum.html")