from django.shortcuts import render
from django.HTTP import HttpResponse

# Create your views here.
def product_home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")