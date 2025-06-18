from django.shortcuts import render, redirect, get_object_or_404
from .decorators import *
from ..models import *
from ..forms import TaskForm

def list(request):
    if request.user.groups.filter(name='main').exists():
        tasks = Tasks.objects.all()
    else:
        tasks = Tasks.objects.filter(user=request.user)

    return render(request, 'index.html', {
        'tasks': tasks,
        'active_tab': 'index'
    })

@in_group('main')
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('all_data', id=task.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/form.html', {'form': form, 'title': 'Добавить задачу'})

def detail(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.user != request.user and not request.user.groups.filter(name='main').exists():
        return redirect('list')
    else:
        context = {
            'task': task,
            'status': task.status.status
        }
        return render(request, 'tasks/detail.html', context)

@in_group('main')
def edit(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/form.html', {'form': form, 'title': 'Изменить задачу'})

@in_group('main')
def delete(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

def accept(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.user == request.user:
        task.status = get_process_status()
        task.save()
    return redirect('detail', id=task.id)

def review(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.user == request.user:
        task.status = get_review_status()
        task.save()
    return redirect('detail', id=task.id)

@in_group('main')
def revision(request, id):
    task = get_object_or_404(Tasks, id=id)
    task.status = get_revision_status()
    task.save()
    return redirect('detail', id=task.id)

@in_group('main')
def complete(request, id):
    task = get_object_or_404(Tasks, id=id)
    task.status = get_complete_status()
    task.save()
    return redirect('detail', id=task.id)

@in_group('main')
def cancel(request, id):
    task = get_object_or_404(Tasks, id=id)
    task.status = get_cancel_status()
    task.save()
    return redirect('detail', id=task.id)