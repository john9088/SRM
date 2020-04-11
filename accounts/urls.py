from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('products/', views.products),
]
