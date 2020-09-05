from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = ('status' , 'products')



class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1' , 'password2']


class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class Addproduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'