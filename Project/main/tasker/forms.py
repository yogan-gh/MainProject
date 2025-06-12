from datetime import date, timedelta
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
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'user': 'Оператор',
            'subject': 'Тема задания',
            'status': 'Статус',
            'start_date': 'Дата выдачи',
            'end_date': 'Дата исполнения',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            today = date.today()
            self.initial['start_date'] = today
            self.initial['end_date'] = today + timedelta(days=30)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

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