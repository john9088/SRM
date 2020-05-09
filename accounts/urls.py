from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('home/', views.home, name = 'home'),
    path('customer/<str:cust_key>/', views.customer,name = 'customers'),
    path('products/', views.products,name = 'products'),
    path('create_order/<str:cust_key>/',views.createOrder,name = 'create_order'),
    path('update_order/<str:order_key>/',views.updateOrder,name = 'update_order'),
    path('delete/<str:order_key>/',views.deleteOrder,name = 'delete_order'),


]
