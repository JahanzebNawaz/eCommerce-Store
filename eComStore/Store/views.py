from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Product, Contact
from .forms import ContactForm
# Create your views here.
from math import ceil


def index(request):
        url = 'Store/index.html'
        products = Product.objects.all()
       

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
        url = 'Store/contact.html'
        if request.method=="POST":
                name = request.POST.get('name', '')
                email = request.POST.get('email', '')
                phone = request.POST.get('phone', '')
                desc = request.POST.get('desc', '')
                contact = Contact(name=name, email=email, phone=phone, desc=desc)
                
                if contact:
                        contact.save()
                        messages.success(request, 'Message Sent Successfully!')
                        return HttpResponseRedirect('/contact/')
                else:
                        messages.error(request, 'Error submiting Message')
                        return render(request, url)
        else:
                return render(request, url)


def tracker(request):
        url = 'Store/tracker.html'

        return render(request, url)

def search(request):
        url = 'Store/search.html'
        return render(request, url)


def product(request, g_id):
        ''' fetch product using the id'''
        product = Product.objects.filter(id=g_id)
        
        url = 'Store/productview.html'        
        return render(request, url, {'product': product[0]})

 
def checkout(request):
        url = 'Store/about.html'
        return render(request, url)