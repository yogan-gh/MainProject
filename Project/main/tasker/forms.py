from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "user",
            "subject",
            "status",
            "start_date",
            "end_date",
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

# Формы для связанных объектов
class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ['person']

class InternetAccountForm(forms.ModelForm):
    class Meta:
        model = InternetAccounts
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'https://example.com'})
        }

class EmailForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'user@example.com'})
        }

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumbers
        fields = ['numbers']
        widgets = {
            'numbers': forms.NumberInput(attrs={'placeholder': '79001234567'})
        }