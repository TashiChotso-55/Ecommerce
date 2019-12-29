from django.shortcuts import render,get_object_or_404,redirect
from homepage.models import Category,Product
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def category(request):
    return render(request,'category.html')

def prodByCat(request,catname):
    c_page=get_object_or_404(Category,slug=catname)
    products_list=Product.objects.filter(category=c_page,available=True)
    paginator=Paginator(products_list,15)
    products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'products':products})


def ProdCatDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})    

def getAllCat(request):
    products_list=Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,15)
    products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'products':products})
