from django.shortcuts import render, redirect
from .form import SignUp
# Create your views here.
def logout_view(request):
    return render(request,'registration/logout.html')


def Signup_view(request):
    form=SignUp()
    if request.method=="POST":
        form=SignUp(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password) # hashing algorithm
            user.save()
            return redirect('/accounts/login')
    return render(request,'registration/signup.html',{'form':form})
