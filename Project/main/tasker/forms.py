from datetime import date, timedelta
from django import forms
from django.contrib.auth.models import Group
from .models import *

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = TaskSubjects
        fields = [
            'name',
            "synonym",
        ]

        labels = {
            'name': 'Название тематики',
            'synonym': 'Обозначение',

        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = [
            "synonym",
        ]
        labels = {
            'synonym': 'Название статуса',
        }

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

        editors_group = Group.objects.get(name='user')  # Замените 'Editors' на нужную группу
        self.fields['user'].queryset = editors_group.user_set.all()

        if not self.instance.pk:
            today = date.today()
            self.initial['start_date'] = today
            self.initial['end_date'] = today + timedelta(days=30)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumbers
        fields = '__all__'
        widgets = {
            'phoneNumbers': forms.NumberInput(attrs={'placeholder': '79001234567'})
        }

class InternetAccountForm(forms.ModelForm):
    class Meta:
        model = InternetAccounts
        fields = '__all__'

class EmailForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = '__all__'
