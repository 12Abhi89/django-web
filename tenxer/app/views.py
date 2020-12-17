from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'abhi'})

def add(request):
    val1=request.GET["num1"]
    val2=request.GET["num2"]
    res = int(val1) + int(val2)
    return render(request,'result.html',{"result":res})

def projects(request):
    return render(request,'projects.html')

def lab(request):
    project = 'us011'
    return render(request,'us011.html')