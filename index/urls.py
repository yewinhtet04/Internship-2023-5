
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='upload'),
    path('test',views.test,name='jfgj')
]
