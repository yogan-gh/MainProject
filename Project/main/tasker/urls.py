from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views
from .myviews import settings, tasks

settings_patterns = [
    path('add_user/', settings.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', settings.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', settings.delete_user, name='delete_user'),

    path('add_subject/', settings.add_subject, name='add_subject'),
    path('edit_subject/<int:subject_id>/', settings.edit_subject, name='edit_subject'),
    path('delete_subject/<int:subject_id>/', settings.delete_subject, name='delete_subject'),

    path('add_status/', settings.add_status, name='add_status'),
    path('edit_status/<int:status_id>/', settings.edit_status, name='edit_status'),
    path('delete_status/<int:status_id>/', settings.delete_status, name='delete_status'),

    path('', settings.all_view, name='all_data'),
]

tasks_patterns = [
    path("", tasks.list, name='list'),
    path("add/", tasks.add, name='add'),
    path("<int:id>/", tasks.detail, name='detail'),
    # path('<int:pk>/data/', tasks.adddata),
    path("<int:id>/edit/", tasks.edit, name='edit'),
    path("<int:id>/delete/", tasks.delete, name='delete'),
]

urlpatterns = [
    path("", RedirectView.as_view(url='task/', permanent=True)),
    path('task/', include(tasks_patterns)),
    path('stats/', views.stats),
    path('settings/', include(settings_patterns)),
    path('feedback/', views.feedback),
]
