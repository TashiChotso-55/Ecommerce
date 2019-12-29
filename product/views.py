from django.shortcuts import render,get_object_or_404,redirect
from homepage.models import Category,Product
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def product(request,prodid):
    product=Product.objects.get(slug=prodid)
    return render(request,'product.html',{'product':product})
