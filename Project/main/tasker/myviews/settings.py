from django.shortcuts import render, redirect, get_object_or_404
from .decorators import *
from ..models import TaskSubjects, TaskStatus
from ..forms import SubjectsForm, StatusForm

@in_group('main')
def all_settings(request):
    context = {
        'subjects': TaskSubjects.objects.all(),
        'statuses': TaskStatus.objects.all(),
        'active_tab': 'settings'
    }
    return render(request, 'settings/settings.html', context)

@in_group('main')
def add_subject(request):
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_settings')
    else:
        form = SubjectsForm()
    return render(request, 'add_subject.html', {'form': form})

@in_group('main')
def edit_subject(request, subject_id):
    subject = get_object_or_404(TaskSubjects, pk=subject_id)
    if request.method == 'POST':
        form = SubjectsForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('all_settings')
    else:
        form = SubjectsForm(instance=subject)
    return render(request, 'settings/edit.html', {'form': form})

@in_group('main')
def delete_subject(request, subject_id):
    subject = get_object_or_404(TaskSubjects, pk=subject_id)
    subject.delete()
    return redirect('all_settings')

@in_group('main')
def add_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_settings')
    else:
        form = StatusForm()
    return render(request, 'add_status.html', {'form': form})

@in_group('main')
def edit_status(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('all_settings')
    else:
        form = StatusForm(instance=status)
    return render(request, 'settings/edit.html', {'form': form})

@in_group('main')
def delete_status(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    status.delete()
    return redirect('all_settings')