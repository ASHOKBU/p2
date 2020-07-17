from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world')
def home(request):
    return HttpResponse('<h1>Welcome to Homepage</h1>')
def html_demo1(request):
    return render(request,"sample1.html")
def html_demo2(request):
    return render(request,"sample2.html")