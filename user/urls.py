from django.urls import path
from . import views

urlpatterns=[
    path('',views.user,name='user from index'),
    path('submit',views.submit,name='submit from index'),
]