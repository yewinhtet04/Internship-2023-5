from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import json
#from . import mongodb
# Create your views here.
from django.http import HttpResponse

def upload(request):
    if request.method=='POST':
        img=request.FILES.getlist('img')
        for i in img:
            f=open('txt.png','w')
            f.write(i)
            print(i)
    return render(request,'upload.html')