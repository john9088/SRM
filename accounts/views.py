from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

def createOrder(request):

	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST) #request.POST contains all the data passed from the form
		#print(f"***DATA:{request.POST}***")
		if form.is_valid():
			form.save()
			return redirect('/accounts/')

	content = {'form':form}

	return render(request,'accounts/order_form.html',content)

def	updateOrder(request,order_key):
	
	
	order = Order.objects.get(id=order_key)
	form = OrderForm(instance = order) #To save the content of the from as data obtained from order

	if request.method == 'POST':
		form = OrderForm(request.POST, instance = order) #request.POST contains all the data passed from the form
		#print(f"***DATA:{request.POST}***")			 #on passing instance=order it saves all the data to current POST request and does not create a new POST request 	
		if form.is_valid():
			form.save()
			return redirect('/accounts/')
	content = {'form':form}
	return render(request,'accounts/order_form.html',content)

def deleteOrder(request,order_key):
	item = Order.objects.get(id=order_key)
	if request.method == 'POST':
		item.delete()
		return redirect('/accounts/')
	content = {'item':item}
	return render(request,'accounts/delete.html',content) 