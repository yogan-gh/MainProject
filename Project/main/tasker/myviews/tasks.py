from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from django.db.models import Case, When, IntegerField
from .decorators import *
from ..models import *
from ..forms import TaskForm

def list(request):
    if request.user.groups.filter(name='main').exists():
        tasks = Tasks.objects.select_related('status', 'user').annotate(
            status_order=Case(
                When(status=get_review_status(), then=1),
                When(status=get_new_status(), then=2),
                When(status=get_revision_status(), then=3),
                When(status=get_process_status(), then=4),
                When(status=get_complete_status(), then=5),
                When(status=get_cancel_status(), then=6),
                default=7,
                output_field=IntegerField(),
            )
        ).order_by('status_order', '-start_date')
    else:
        tasks = Tasks.objects.filter(user=request.user).select_related('status', 'user').annotate(
            status_order=Case(
                When(status=get_new_status(), then=1),
                When(status=get_revision_status(), then=2),
                When(status=get_process_status(), then=3),
                When(status=get_review_status(), then=4),
                When(status=get_complete_status(), then=5),
                When(status=get_cancel_status(), then=6),
                default=7,
                output_field=IntegerField(),
            )
        ).order_by('status_order', '-start_date')

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

def download_file(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.file:
        response = FileResponse(task.file.open(), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{task.file_name}"'
        return response
    raise Http404("Файл не найден")

def upload_file(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        if 'delete_file' in request.POST and task.file:
            # Удаление существующего файла
            task.file.delete()
            task.file_name = None
            task.save()
        elif 'file' in request.FILES:
            # Загрузка нового файла
            if task.file:
                task.file.delete()  # Удаляем старый файл
            file = request.FILES['file']
            task.file = file
            task.file_name = file.name
            task.save()
        return redirect('detail', id=task.id)
    return redirect('detail', id=task.id)