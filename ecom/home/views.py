from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from authantication.form import FeedbackForm
from django.contrib import messages
from .models import Address


# Create your views here.

def home_view(request):
    data=Product.objects.all()
    return render(request, 'html/home.html',{'data':data})

@login_required
def profile_view(request):
    address = Address.objects.filter(user=request.user).last()
    return render(request,'html/profile.html',{'user':request.user,'address':address})


def about_view(request):
    return render(request,'html/about.html')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been submitted.")
            return redirect('/') 
    else:
        form = FeedbackForm()
    return render(request, 'html/feedback.html', {'form': form})

from .forms import Add_address

@login_required
def add_address(request):
    if request.method == 'POST':
        form = Add_address(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user   
            address.save()
            return redirect('/profile') 
    else:
        form = Add_address()
    return render(request, 'html/address.html', {'form': form})
