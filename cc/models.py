from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    CATEGORY = (
        ('Active','Active'),
        ('Moderately active','Moderately active'),
        ('Inactive','Inactive')
    )
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=100,unique=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, null=True)
    weight = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    height = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    category = models.CharField(max_length=50, choices=CATEGORY)


class Food(models.Model):
    CATEGORY = (
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Snacks','Snacks')
    )
    item = models.CharField(max_length=100, null=True)
    calorieAmount = models.DecimalField(max_digits=7,decimal_places=3,null=True)
    carbAmount = models.DecimalField(max_digits=7,decimal_places=3,null=True)
    proteinAmount = models.DecimalField(max_digits=7,decimal_places=3,null=True)
    fatAmount = models.DecimalField(max_digits=7,decimal_places=3,null=True)
    weightofItem = models.DecimalField(max_digits=10,decimal_places=3,null=True)
    category = models.CharField(max_length=40, choices=CATEGORY)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)