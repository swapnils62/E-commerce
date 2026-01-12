from django.contrib import admin
from .models import Product

# Register your models here.
class Productadmin(admin.ModelAdmin):
    list_display=['id', 'name', 'image', 'discription', 'quantity']

admin.site.register(Product,Productadmin)