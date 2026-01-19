from django.db import models
from django.contrib.auth.models import User
from home.models import Product,Address
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('placed', 'Placed'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='placed'
    )

class Orderitem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()
    subtotal=models.IntegerField()
