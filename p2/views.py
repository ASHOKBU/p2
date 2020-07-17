from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')
def home(request):
    return HttpResponse('<h1>Welcome to Homepage</h1>')
