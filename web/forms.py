from django import forms
from .models import student


class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['profile', 'first_name', 'last_name', 'email', 'password','City']
        
        
        
        