from django.shortcuts import HttpResponse, render
from datetime import datetime
from products.models import Product


# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        posts = Product.objects.all()

        context = {
            'posts': posts
        }
        return render(request, 'products/products.html', context=context)
