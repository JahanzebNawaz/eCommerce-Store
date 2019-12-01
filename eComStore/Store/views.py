from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Product, Contact, Orders, OrderUpdate
from .forms import ContactForm
# Create your views here.
from math import ceil
import json


def index(request):
    url = 'Store/index.html'
    try:
        products = Product.objects.all()
    except Product.DoestNotExist:
        return HttpResponse('Error fetching data from database')

    all_products = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        no_slides = n//4 + ceil((n/4)-(n//4))
        all_products.append([prod, range(1, no_slides), no_slides])

    params = {'product': products, 'all_product': all_products}
    return render(request, url, params)


def search_match(query, item):
    ''' match query of user with items in database '''
    if query in item.desc.lower() or query in item.product_name.lower():
        return True
    else:
        return False


def search(request):
    url = 'Store/index.html'
    query = request.GET.get('search')
    try:
        products = Product.objects.all()
    except Product.DoestNotExist:
        return HttpResponse('Error fetching data from database')

    all_products = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}

    for cat in cats:
        prodtemp = Product.objects.filter(product_category=cat)
        prod = [item for item in prodtemp if search_match(query, item)]
        n = len(prod)
        no_slides = n//4 + ceil((n/4)-(n//4))
        all_products.append([prod, range(1, no_slides), no_slides])

    params = {'product': products, 'all_product': all_products}
    return render(request, url, params)


def about(request):
    url = 'Store/about.html'
    return render(request, url)


def contact(request):
    url = 'Store/contact.html'
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        try:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
        except Contact.DoesNotExist:
            return redirect('contact')

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
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        [updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    url = 'Store/tracker.html'
    return render(request, url)


def product(request, g_id):
    ''' fetch product using the id'''
    try:
        product = Product.objects.filter(id=g_id)
    except Product.DoesNotExist:
        return redirect('index')
    url = 'Store/productview.html'
    return render(request, url, {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        try:
            order = Orders(items_json=items_json, name=name, email=email,
                           address=address, city=city, state=state,
                           zip_code=zip_code, phone=phone, amount=amount)
            if order:
                order.save()
                messages.success(
                    request, 'Successfully Order submitted! ')
            else:
                messages.error(request, 'Error submitting  Order!')
                return redirect('index')

        except Orders.DoesNotExist:
            return redirect('checkout')

        thank = True
        id = order.order_id
        return render(request, 'Store/checkout.html', {'thank': thank,
                                                       'id': id})

    url = 'Store/checkout.html'
    return render(request, url)
