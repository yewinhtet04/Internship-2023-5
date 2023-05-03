from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(req):
    return HttpResponse('This is home from shop')
def detail(req):
    return HttpResponse('This is detail from shop')
def cart(req):
    return HttpResponse('This is cart from shop')