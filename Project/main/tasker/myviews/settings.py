from django.shortcuts import render, redirect, get_object_or_404
from ..models import Users, TaskSubjects, TaskStatus
from ..forms import UserForm, SubjectsForm, StatusForm

def all_data_view(request):
    context = {
        'users': Users.objects.all(),
        'subjects': TaskSubjects.objects.all(),
        'statuses': TaskStatus.objects.all()
    }
    return render(request, 'settings.html', context)

# Users CRUD
def users_view(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    user.delete()
    return redirect('all_data')

# TaskSubjects CRUD
def subjects_view(request):
    subjects = TaskSubjects.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = SubjectsForm()
    return render(request, 'add_subject.html', {'form': form})

def edit_subject(request, subject_id):
    subject = get_object_or_404(TaskSubjects, pk=subject_id)
    if request.method == 'POST':
        form = SubjectsForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = SubjectsForm(instance=subject)
    return render(request, 'edit_subject.html', {'form': form})

def delete_subject(request, subject_id):
    subject = get_object_or_404(TaskSubjects, pk=subject_id)
    subject.delete()
    return redirect('all_data')

# TaskStatus CRUD
def statuses_view(request):
    statuses = TaskStatus.objects.all()
    return render(request, 'statuses.html', {'statuses': statuses})

def add_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = StatusForm()
    return render(request, 'add_status.html', {'form': form})

def edit_status(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = StatusForm(instance=status)
    return render(request, 'edit_status.html', {'form': form})

def delete_status(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    status.delete()
    return redirect('all_data')