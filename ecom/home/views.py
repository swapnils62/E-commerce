from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from authantication.form import FeedbackForm
from django.contrib import messages


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
