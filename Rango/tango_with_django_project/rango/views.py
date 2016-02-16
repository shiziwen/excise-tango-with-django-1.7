from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!<br/><a href="/rango/about">About</a>')

def about(request):
    return HttpResponse('<a href="/rango/">Index</a></br>Rango says here is the about page.')