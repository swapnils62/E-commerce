from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    data=Product.objects.all()
    return render(request, 'html/home.html',{'data':data})

@login_required
def home2_view(request):
    user=request.user
    data=Product.objects.all()
    return render(request, 'html/loginhome.html',{'user':user,'data':data})

@login_required
def profile_view(request):
    return render(request,'html/profile.html',{'user':request.user})
