from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return HttpResponse('This is from polls home!')


def polls(request):
    if request.method == "GET":
        img = request.GET['img']
        return render(request, 'poll.html', {'img': img})
    return render(request, 'poll.html')
