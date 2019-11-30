from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
from math import ceil


def index(request):
        url = 'Store/index.html'
        products = Product.objects.all()
        # n = len(products)
        # no_slides = n//4 + ceil((n/4)-(n//4))

        # all_products = [[products, range(1, no_slides), no_slides], [products, range(1, no_slides), no_slides]]

        all_products = []
        catprods = Product.objects.values('product_category', 'id')
        cats = {item['product_category'] for item in catprods}

        for cat in cats:
                prod = Product.objects.filter(product_category = cat)
                n = len(prod)
                no_slides = n//4 + ceil((n/4)-(n//4)) 
                all_products.append([prod, range(1, no_slides), no_slides])

        params = { 'product': products, 'all_product': all_products}
        return render(request, url, params)


def about(request):
        url = 'Store/about.html'
        return render(request, url)


def contact(request):
        return HttpResponse("Contact Page")


def tracker(request):
        return HttpResponse("tracker Page")


def search(request):
        return HttpResponse("search Page")


def product(request):
        return HttpResponse("product Page")


def checkout(request):
        return HttpResponse("checkout Page")