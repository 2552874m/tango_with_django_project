from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def index(request):
    #Rango says hey there partner!
    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    #Rango says here is the about page.
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

    return render(request, 'rango/about.html')