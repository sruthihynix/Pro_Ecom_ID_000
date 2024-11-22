from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:4]

    latest_products = Product.objects.order_by('-id')[:4]#
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html', context)

def list_products(request):
    # Mark 1: Get the page number from the request, default to 1 if not provided
    page=1
    if request.GET:
        page=request.GET.get('page',1)

    product_list=Product.objects.order_by('priority') #(-priority-> reverse order of priority)
    # Mark 3: Create a paginator object, showing 2 products per page
    product_paginator=Paginator(product_list,3)
    # Mark 4: Get the products for the current page-page
    product_list=product_paginator.get_page(page)

    # Mark 5: Pass the paginated products to the template
    context = {'products': product_list}
    # print(product_list)
    # print(context)
    return render(request,'product_page.html', context)
## before paginator----------------------
# def list_products(request):
#      product_list=Product.objects.filter()
#     context = {'products': 'product_list'}
#     print(product_list)
#     # print(context)
#     return render(request,'product_page.html', context)
def detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    context={'product': product}

    return render(request,'product_detail.html',context)