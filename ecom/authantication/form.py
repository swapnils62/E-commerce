from django import forms
from django.contrib.auth.models import User
from home.models import Feedback


class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']