from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
    
    
    context = {
        
    }
    return render(request, 'main.html',context)
    # Create your views here.
