from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='This is home from shop'),
    path('detail/',views.detail,name='detail from shop'),
    path('cart/',views.cart,name='cart from shop'),
]