from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #Rango says hey there partner!
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    #Rango says here is the about page.
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")