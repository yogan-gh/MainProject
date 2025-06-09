from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.forms import formset_factory
from .forms import *

def index(request):
    tasks = Tasks.objects.all()
    return render(request,
                  "index.html",
                  {'active_tab': 'index', "tasks": tasks})

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect(f'{task.id}/adddata/')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form': form})


def adddata(request, id):
    task = get_object_or_404(Tasks, id=id)

    # Создаем formsets для каждого типа объектов
    PersonFormSet = formset_factory(PersonForm, extra=1)
    InternetAccountFormSet = formset_factory(InternetAccountForm, extra=1)
    EmailFormSet = formset_factory(EmailForm, extra=1)
    PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=1)

    if request.method == 'POST':
        person_formset = PersonFormSet(request.POST, prefix='persons')
        internet_formset = InternetAccountFormSet(request.POST, prefix='internet')
        email_formset = EmailFormSet(request.POST, prefix='emails')
        phone_formset = PhoneNumberFormSet(request.POST, prefix='phones')

        all_valid = all([
            person_formset.is_valid(),
            internet_formset.is_valid(),
            email_formset.is_valid(),
            phone_formset.is_valid()
        ])

        if all_valid:
            # Сохраняем persons
            for form in person_formset:
                if form.has_changed():
                    person = form.save()
                    task.persons.add(person)

            # Сохраняем internet accounts
            for form in internet_formset:
                if form.has_changed():
                    account = form.save()
                    task.internet_accounts.add(account)

            # Сохраняем emails
            for form in email_formset:
                if form.has_changed():
                    email = form.save()
                    task.emails.add(email)

            # Сохраняем phone numbers
            for form in phone_formset:
                if form.has_changed():
                    phone = form.save()
                    task.phoneNumbers.add(phone)

            return redirect(f'/tasker/{id}')
    else:
        person_formset = PersonFormSet(prefix='persons')
        internet_formset = InternetAccountFormSet(prefix='internet')
        email_formset = EmailFormSet(prefix='emails')
        phone_formset = PhoneNumberFormSet(prefix='phones')

    context = {
        'task': task,
        'person_formset': person_formset,
        'internet_formset': internet_formset,
        'email_formset': email_formset,
        'phone_formset': phone_formset,
    }
    return render(request, 'adddata.html', context)

def detail(request, id):
    task = Tasks.objects.get(id=id)
    return render(request,
                  "detail.html",
                  {'active_tab': 'task-details', "task": task})

def edit(request, id):
    return HttpResponse(f"<h2>ID: {id}")

def delete(request, id):
    return HttpResponse(f"<h2>ID: {id}")

def stats(request):
    return render(request, "stats.html", {'active_tab': 'stats'})

def settings(request):
    return render(request, "settings.html", {'active_tab': 'settings'})

def feedback(request):
    return render(request, "feedback.html", {'active_tab': 'feedback'})