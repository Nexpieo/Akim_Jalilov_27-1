from django.shortcuts import HttpResponse, render
from datetime import datetime
from products.models import Product


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
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)
