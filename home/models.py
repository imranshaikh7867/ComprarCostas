
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to = "product/images", default = "")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    zip = models.CharField(max_length=200, default="")
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.email
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to = "customer/image", default = "")
    address = models.TextField()


class Payment(models.Model):
    card_number = models.IntegerField()
    card_holder = models.CharField(max_length=200, default="")
    cvv = models.IntegerField()

    def __str__(self):
        return self.card_number

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=100000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default="")
    address = models.TextField()
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    zip = models.CharField(max_length=200, default="")
    card_number = models.IntegerField()
    card_holder = models.CharField(max_length=200, default="")
    cvv = models.IntegerField()

    def __str__(self):
        return self.name

class Tracker(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:7] + "....."