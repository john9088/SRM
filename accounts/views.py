from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()

	orders_delivered = orders.filter(status = 'Delivered').count()
	orders_pending = orders.filter(status = 'Pending').count()

	container = {'orders':orders , 'customers': customers,
	'total_orders':total_orders,'total_customers':total_customers,
	'orders_delivered':orders_delivered,'orders_pending':orders_pending}
	
	return render(request, 'accounts/dashboard.html',container)

def customer(request,cust_key):
	customer = Customer.objects.get(id = cust_key)
	orders = customer.order_set.all()
	order_count = orders.count()
	container = {'customer':customer,'orders':orders,'order_count':order_count}
	return render(request, 'accounts/customer.html',container)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html',{'products':products})