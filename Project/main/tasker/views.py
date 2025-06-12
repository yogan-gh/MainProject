from django.shortcuts import render

def stats(request):
    return render(request, "stats.html", {'active_tab': 'stats'})

def settings(request):
    return render(request, "settings.html", {'active_tab': 'settings'})

def feedback(request):
    return render(request, "feedback.html", {'active_tab': 'feedback'})