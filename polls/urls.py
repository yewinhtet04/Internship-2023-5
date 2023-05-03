from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index from polls"),
    path("index/", views.index, name="index from polls"),
    path("home/",views.home,name="home from p")
]