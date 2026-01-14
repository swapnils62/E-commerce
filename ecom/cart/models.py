from django.db import models
from django.contrib.auth.models import User
from home.models import Product
# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

class Cart_item(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

