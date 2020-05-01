from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__' #if you want to show only few fields then pass a list like ['customer','products']