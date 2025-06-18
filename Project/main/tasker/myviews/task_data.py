from django.shortcuts import render, redirect, get_object_or_404
from .decorators import *
from ..models import Tasks, Persons, PhoneNumbers, InternetAccounts, Emails
from ..forms import PersonForm, PhoneNumberForm, InternetAccountForm, EmailForm

@in_group('main')
def all_data(request, id):
    task = get_object_or_404(Tasks, id=id)
    context = {
        'task': task,
        'persons': task.persons.all(),
        'phones': task.phoneNumbers.all(),
        'accounts': task.accounts.all(),
        'emails': task.emails.all(),
    }
    return render(request, 'tasks/data.html', context)

@in_group('main')
def add_person(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            task.persons.add(person)
            return redirect('all_data', id=id)
    else:
        form = PersonForm()
    return render(request, 'add_person', {'form': form})

@in_group('main')
def delete_person(request, id, person_id):
    task = get_object_or_404(Tasks, id=id)
    person = get_object_or_404(Persons, pk=person_id)
    task.persons.remove(person)
    return redirect('all_data', id=id)

@in_group('main')
def add_phone(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone = form.save()
            task.phoneNumbers.add(phone)
            return redirect('all_data', id=id)
    else:
        form = PhoneNumberForm()
    return render(request, 'add_phone', {'form': form})

@in_group('main')
def delete_phone(request, id, phone_id):
    task = get_object_or_404(Tasks, id=id)
    phone = get_object_or_404(PhoneNumbers, pk=phone_id)
    task.phoneNumbers.remove(phone)
    return redirect('all_data', id=id)

@in_group('main')
def add_account(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        form = InternetAccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            task.accounts.add(account)
            return redirect('all_data', id=id)
    else:
        form = InternetAccountForm()
    return render(request, 'add_account', {'form': form})

@in_group('main')
def delete_account(request, id, account_id):
    task = get_object_or_404(Tasks, id=id)
    account = get_object_or_404(InternetAccounts, pk=account_id)
    task.accounts.remove(account)
    return redirect('all_data', id=id)

@in_group('main')
def add_email(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save()
            task.emails.add(email)
            return redirect('all_data', id=id)
    else:
        form = EmailForm()
    return render(request, 'add_email', {'form': form})

@in_group('main')
def delete_email(request, id, email_id):
    task = get_object_or_404(Tasks, id=id)
    email = get_object_or_404(Emails, pk=email_id)
    task.emails.remove(email)
    return redirect('all_data', id=id)