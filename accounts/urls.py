from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('customer/<str:cust_key>/', views.customer),
    path('products/', views.products),
]
