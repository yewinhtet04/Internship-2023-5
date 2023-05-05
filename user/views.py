from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.http import HttpResponse


def user(request):
    if request.method=='POST':
        return request(request,"user.html",{'name':'1234'})
    return render(request,"user.html")

def submit(request):
    if request.method=='POST':
        return request(request,"submit.html",{})
        #return HttpResponse('hi')
    return render(request,"user.html")

