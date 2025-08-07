from django.shortcuts import render

from django.http import HttpResponse
from .models import Product

# Create your views here.

# use name index for main page of app

# /products -> index need to map this
def index(request): # http requests from the url, 
    products = Product.objects.all() # or .filter() or .get() or .save()


    return render(request, 
                  'index.html', 
                  {'products': products})

def new(request):
    return HttpResponse('New Products')