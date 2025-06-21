from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count, FloatField, ExpressionWrapper
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .myviews import decorators
from .models import Tasks, TaskStatus, CustomUser
from datetime import datetime

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        return redirect('login')

@login_required
def stats_view(request):
    user_id = request.GET.get('user', 'all')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    users = CustomUser.objects.filter(is_superuser=False)

    filter_info = {}

    # Проверка прав
    if request.user.groups.filter(name='user').exists() and not request.user.is_superuser:
        if 'user' in request.GET and int(request.GET.get('user')) != request.user.id:
            raise PermissionDenied("Доступ только к своей статистике")

    # Для обычных пользователей показываем только их статистику
    if request.user.groups.filter(name='user').exists() and not request.user.groups.filter(name='main').exists():
        tasks = Tasks.objects.filter(user=request.user)
        filter_info['user'] = CustomUser.objects.get(id=request.user.id)
        show_user_filter = False
    else:
        tasks = Tasks.objects.all()
        show_user_filter = True

    # Фильтрация по пользователю
    if user_id != 'all':
        try:
            user = CustomUser.objects.get(id=user_id)
            tasks = tasks.filter(user=user)
            filter_info['user'] = user
        except CustomUser.DoesNotExist:
            pass

    # Фильтрация по дате
    if date_from:
        date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
        tasks = tasks.filter(start_date__gte=date_from)
        filter_info['date_from'] = date_from.strftime('%d.%m.%Y')
    if date_to:
        date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        tasks = tasks.filter(start_date__lte=date_to)
        filter_info['date_to'] = date_to.strftime('%d.%m.%Y')

    status_stats = tasks.values('status__status', 'status__synonym').annotate(
        count=Count('id')
    ).order_by('status__status')

    total_tasks = tasks.count()

    status_stats = []
    if total_tasks > 0:
        status_stats = tasks.values('status__status', 'status__synonym').annotate(
            count=Count('id')
        ).annotate(
            percentage=ExpressionWrapper(
                100.0 * Count('id') / total_tasks,
                output_field=FloatField()
            )
        ).order_by('status__status')

    context = {
        'users': users,
        'status_stats': status_stats,
        'show_user_filter': show_user_filter,
        'selected_user': int(user_id) if user_id != 'all' else 'all',
        'date_from': date_from.strftime('%Y-%m-%d') if date_from else '',
        'date_to': date_to.strftime('%Y-%m-%d') if date_to else '',
        'total_tasks': total_tasks,
        'filter_info': filter_info
    }
    return render(request, 'stats.html', context)

@decorators.in_group('main')
def settings(request):
    return render(request, "settings.html", {'active_tab': 'settings'})

@login_required
def feedback(request):
    return render(request, "feedback.html", {'active_tab': 'feedback'})