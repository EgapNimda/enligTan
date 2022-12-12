
from django.http import HttpResponse
from django.template import loader
from chanting.time import monk_day
from django.shortcuts import render

# def main(request):

#     if monk_day():
#         s = "วันนี้วันพระ"
    
#     else:
#         s = ""
#     context = {
#         "monk" : s
#     }
#     return render(request,"main.html",context)

def main(request):
    context = {}

    '''if monk_day():
        s = "วันนี้วันพระ"

    else:
        s = ""    '''
    n = monk_day()
    if(n == 0):
        context = {'monk' : "วันนี้วันพระ"}
    elif(n == 1):
        context = {'monk' : "พรุ่งนี้วันพระ"}
    elif(n == -1):
        context = {'monk' : "หมดปีแล้วจ้า:)"}
    else:
        context = {'monk' : "อีก " + str(n) + " วันจะถึงวันพระ"}
    return render(request,"main.html",context)
def viewProfile(request):
  
    return render(request, "viewProfile.html")

def suadPrajum(request):
    return render(request, "suadPrajum.html")