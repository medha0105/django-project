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
        ('Female','Female'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=100,unique=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    gender = models.CharField(max_length=50, null=True, choices=GENDER)
    category = models.CharField(max_length=50, null=True,choices=CATEGORY)

    def __str__(self):
        return self.name


class Food(models.Model):
    FOOD_CATEGORY = (
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Snacks','Snacks')
    )
    item = models.CharField(max_length=100, null=True)
    calories = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    proteins = models.FloatField(null=True)
    fats = models.FloatField(null=True)
    # weight = models.FloatField(null=True)
    food_category = models.CharField(max_length=40,null=True,choices=FOOD_CATEGORY)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.item
