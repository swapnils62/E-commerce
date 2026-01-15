from django import forms
from .models import Address

class Add_address(forms.ModelForm):
    class Meta:
        model=Address
        exclude = ['user']