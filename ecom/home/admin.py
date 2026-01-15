from django.contrib import admin
from .models import Product
from .models import Feedback, Address

# Register your models here.
class Productadmin(admin.ModelAdmin):
    list_display=['id', 'name', 'image', 'discription', 'quantity']

admin.site.register(Product,Productadmin)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    # This adds a search bar to find specific feedback
    search_fields = ['name', 'email']
    # This adds a date filter on the right side
    list_filter = ['created_at',]

class AddressAdmin(admin.ModelAdmin):
    list_display=['id',"address",'city','state','country','pincode']

admin.site.register(Address,AddressAdmin)