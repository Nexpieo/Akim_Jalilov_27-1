from django.shortcuts import HttpResponse
from datetime import datetime

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
