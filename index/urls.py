from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home from index'),
    path('',views.home,name='home from index'),
    path('about/',views.about,name='about from index'),
    path('generate',views.generate,name='contact from index'),
]