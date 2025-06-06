from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Tasks
from .forms import TaskForm

def index(request):
    tasks = Tasks.objects.all()
    return render(request,
                  "index.html",
                  {'active_tab': 'index', "tasks": tasks})

def create(request):
    if request.method == "POST":
        task = Tasks()
        task.user = request.POST.get("user")
        task.subject = request.POST.get("subject")
        task.status = request.POST.get("status")
        task.start_date = request.POST.get("start_date")
        task.end_date = request.POST.get("end_date")
        task.save()
    taskForm = TaskForm()
    return render(request, "create.html", {"form": taskForm})

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