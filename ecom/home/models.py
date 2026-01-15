from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField()
    discription=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField(default=0)



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"