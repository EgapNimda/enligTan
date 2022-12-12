
from django.http import HttpResponse
from django.template import loader
from chanting.time import monk_day
from django.shortcuts import render
from .models import praying, prayingset


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


def chanting(request,title):
    if(praying.objects.filter(title = title)):
        ch = praying.objects.get(title = title)
        content = ch.content
        context ={
            "title" : title,
            "content" : content
        }
    else:
        context = {
            "title" : title,
            "content" : "ไม่พบข้อมูลในคลังบทสวด"
        }
    return render(request,"chanting.html",context)

def suadPrajum(request):
    return render(request, "suadPrajum.html")
def totalD(request):
    return render(request, "totalD.html")

