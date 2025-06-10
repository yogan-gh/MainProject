from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = TaskSubjects
        fields = '__all__'

class StatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = '__all__'

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
        fields = ['account']

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