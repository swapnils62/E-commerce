from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField()
    discription=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField(default=0)