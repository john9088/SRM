from django.db import models

# Steps tp add models
#Make class of the model you want to add
#The variable in the class will act as your field value
#Once the class is ready in your cmd type python manage.py makemigrations
#And the python manage.py migrate
#After all this make an entry in admin.py to show the added model in admin page

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length = 200, null = True)
	phone = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_length = 200, null = True)
	date_created = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 200, null = True)
	
	def __str__(self):
		return self.name 

class Product(models.Model):
	CATEGORY = (
	 		('Indoor','Indoor'),
	 		('Out Door','Out Door'),
	 	)
	name = models.CharField(max_length = 200, null = True)
	price = models.FloatField(null = True)
	category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
	description = models.CharField(max_length = 200, null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name



class Order(models.Model):
	STATUS = (
			('Pending','Pending'),
			('Out for Delivery','Out for Delivery'),
			('Delivered','Delivered'),
		)
	customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL) #Order inherits from customer and on deleting the customer the order remains with null value currosponding to the deleted customer
	products = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL) #Order inherits from products and on deleting the product the order remains with null value currosponding to the deleted product
	date_created = models.DateTimeField(auto_now_add = True) 
	status = models.CharField(max_length = 200, null = True, choices = STATUS)