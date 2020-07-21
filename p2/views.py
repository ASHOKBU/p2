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

def third(request):
    return render(request,"directory/third.html",context={'data':"Ashok",'name':"Shankar"})

def fourth(request):
    fruits=["apple","banana","grapes","orange"]
    return render(request,"directory/fourth.html",context={'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",context={'a':10,'b':20})