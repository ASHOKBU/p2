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

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,ab):
    a=ab.split(" ")
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))

def pq(request,p,q):
    sum=int(p)+int(q)
    return HttpResponse(str(sum))

def great(request,a,b):
    if int(a) > int(b) :
        greatest=str(a)+" is greater"
    else:
        greatest=str(b)+" is greater"
    return HttpResponse(str(greatest))