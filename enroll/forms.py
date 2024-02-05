from django import forms
from .models import Student
from django.core import validators

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-input','placeholder':'Full Name'}),
            'email': forms.EmailInput(attrs={'class':'form-input', 'placeholder':'Email ID'}),
            'password': forms.PasswordInput(attrs={'class':'form-input'})
        }
