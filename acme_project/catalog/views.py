#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def product_list(request):
    return HttpResponse('<h1>catalog_1</h1>') 
    
def product_detail(request):
    return HttpResponse('<h2>catalog</h2>')
