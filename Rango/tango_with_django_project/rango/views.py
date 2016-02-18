from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "bold message"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse('<a href="/rango/">Index</a></br>Rango says here is the about page.')