from django.shortcuts import render, redirect, get_object_or_404
from ..models import Tasks
from ..forms import TaskForm

def list(request):
    tasks = Tasks.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskForm()
    return render(request, 'tasks/form.html', {'form': form, 'title': 'Добавить задачу'})

def detail(request, id):
    task = get_object_or_404(Tasks, id=id)
    return render(request, 'tasks/detail.html', {'task': task})

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

def delete(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})