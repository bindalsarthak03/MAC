from heapq import nsmallest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    products = Product.objects.all()
    nSlides = len(products)//4 + ceil((len(products)/4 - len(products)//4))
    params = {'number_of_slides': nSlides,'range': (1,nSlides), 'product': products}
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def  productView(request):
    return HttpResponse("We are at Product view page")

def checkout(request):
    return HttpResponse("We are at checkout")