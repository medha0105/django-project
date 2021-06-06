from django.db import models

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
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=100,unique=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, null=True)
    weight = models.DecimalField()
    height = models.DecimalField()
    gender = models.CharField(max_length=50, choices=GENDER)
    category = models.CharField(max_length=50, choices=CATEGORY)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)