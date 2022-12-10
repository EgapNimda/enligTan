from django.shortcuts import render
'''from menu.time import monk_day'''
# Create your views here.

def home(request):
    return render(request, "main.html")
    '''s = ""
    if monk_day() :
        s = "วันนี้วันพระ"
    context = {
        "monk" : s
    }
    return render(request, 'main.html')'''


