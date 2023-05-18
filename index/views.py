from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import json
#from . import mongodb
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'index.html',{'movie':[1,2,3,4]})

def test(request):
    return render(request,'index3.html')