
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('upload/',views.upload),
    path('',views.index),
    path('text/',views.text),
]
