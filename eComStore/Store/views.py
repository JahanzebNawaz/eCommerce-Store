from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
        url = 'Store/index.html'
        return render(request, url)


def about(request):
        return HttpResponse("<h2>About Page</h2>")


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