from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from chanting.time import monk_day
def main(request):

    if monk_day():
        s = "วันนี้วันพระ"
    
    else:
        s = ""
    context = {
        "monk" : s
    }
    return render(request,"main.html",context)


