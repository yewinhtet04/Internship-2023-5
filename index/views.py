from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
def home(request):
    template = loader.get_template('index.html')
    return render(request,'index.html',{})
    #return HttpResponse('This is homr from index')
def about(request):
    return HttpResponse('This is about us from index')
def generate(request):
    if request.method=='POST':
         name=request.POST['name']
         town=request.POST['town']
         age=request.POST['age']
         data={'name':name,'town':town,'age':age,'nickname':name.split(' ')[0]}
         return render(request,'generate.html',data)
         print('NAME')
    else:print('vdknv')
    return HttpResponse('This is contact from index')