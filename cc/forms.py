from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms
from .models import Customer,Food

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['weight','height','age','gender','category']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['item','calories','carbs','proteins','fats','food_category','customer']
        