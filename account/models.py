from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to="product_image")
    options=(
        ("Smartphone","Smartphone"),
        ("Tablet","Tablet"),
        ("Smartwatch","Smartwatch"),
        ("Laptop","Laptop"),
    )
    category=models.CharField(max_length=100,choices=options)
    def __str__(self) :
        return self.title

class Cart(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    quality=models.IntegerField(default=1)

class Order(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField()
    options=(
        ("orderplaced","orderplaced"),
        ("Shipped","Shipped"),
        ("Outfordelivery","Outfordelivery"),
        ("Delivered","Delivered"),
        ("Cancelled","Cancelled")
    )
    status=models.CharField(max_length=100,default="orderplaced")



