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
    age = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    category = models.CharField(max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.name


class Food(models.Model):
    CATEGORY = (
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Snacks','Snacks')
    )
    item = models.CharField(max_length=100, null=True)
    calorieAmount = models.FloatField(null=True)
    carbAmount = models.FloatField(null=True)
    proteinAmount = models.FloatField(null=True)
    fatAmount = models.FloatField(null=True)
    weightofItem = models.FloatField(null=True)
    category = models.CharField(max_length=40, choices=CATEGORY)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)