from django.contrib import admin
from .models import Cart, Cart_item
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']

admin.site.register(Cart, CartAdmin)
admin.site.register(Cart_item, CartItemAdmin)
