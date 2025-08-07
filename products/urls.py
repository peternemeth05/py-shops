from django.urls import path # can map a url to a view function
from . import views # . means current folder



# app starts at 
# /products
# /products/1/detail



urlpatterns = [ 
    path('', views.index),
    path('new/', views.new) # first arg is the url endpoint, in this case it is empty because it is the root
]