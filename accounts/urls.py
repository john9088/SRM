from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('home/', views.home, name = 'home'),
    path('customer/<str:cust_key>/', views.customer,name = 'customers'),
    path('products/', views.products,name = 'products'),
]
