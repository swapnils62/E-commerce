from django.shortcuts import render
from .models import Product

# Create your views here.

def home_view(request):
    data=Product.objects.all()
    return render(request, 'html/home.html',{'data':data})

