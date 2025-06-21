from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .myviews import decorators

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        return redirect('login')

@login_required
def stats(request):
    return render(request, "stats.html", {'active_tab': 'stats'})

@decorators.in_group('main')
def settings(request):
    return render(request, "settings.html", {'active_tab': 'settings'})

@login_required
def feedback(request):
    return render(request, "feedback.html", {'active_tab': 'feedback'})