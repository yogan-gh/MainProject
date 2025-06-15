from django.shortcuts import render
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        return redirect('login')

def stats(request):
    return render(request, "stats.html", {'active_tab': 'stats'})

def settings(request):
    return render(request, "settings.html", {'active_tab': 'settings'})

def feedback(request):
    return render(request, "feedback.html", {'active_tab': 'feedback'})