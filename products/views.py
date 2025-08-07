from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# use name index for main page of app

# /products -> index need to map this
def index(request): # http requests from the url, 
    return HttpResponse('Hello World')

def new(request):
    return HttpResponse('New Products')