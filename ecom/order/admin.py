from django.contrib import admin
from .models import Order,Orderitem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user','address','total_amount','status']

admin.site.register(Order,OrderAdmin)

class OrderitemAdmin(admin.ModelAdmin):
    list_display=['id','order','product','price','quantity','subtotal']

admin.site.register(Orderitem,OrderitemAdmin)