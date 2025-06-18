from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views
from .myviews import settings, tasks, task_data

settings_patterns = [
    path('add_subject/', settings.add_subject, name='add_subject'),
    path('edit_subject/<int:subject_id>/', settings.edit_subject, name='edit_subject'),
    path('delete_subject/<int:subject_id>/', settings.delete_subject, name='delete_subject'),

    path('add_status/', settings.add_status, name='add_status'),
    path('edit_status/<int:status_id>/', settings.edit_status, name='edit_status'),

    path('', settings.all_settings, name='all_settings'),
]

task_data_patterns = [
    path('add_person', task_data.add_person, name='add_person'),
    path('delete_person/<int:person_id>/', task_data.delete_person, name='delete_person'),

    path('add_phone', task_data.add_phone, name='add_phone'),
    path('delete_phone/<int:phone_id>/', task_data.delete_phone, name='delete_phone'),

    path('add_account', task_data.add_account, name='add_account'),
    path('delete_account/<int:account_id>/', task_data.delete_account, name='delete_account'),

    path('add_email', task_data.add_email, name='add_email'),
    path('delete_email/<int:email_id>/', task_data.delete_email, name='delete_email'),
    
    path('', task_data.all_data, name='all_data'),
]

tasks_patterns = [
    path("", tasks.list, name='list'),
    path("add/", tasks.add, name='add'),
    path("<int:id>/", tasks.detail, name='detail'),
    path('<int:id>/data/', include(task_data_patterns)),
    path("<int:id>/edit/", tasks.edit, name='edit'),
    path("<int:id>/delete/", tasks.delete, name='delete'),
]

urlpatterns = [
    path("", views.home_redirect, name='home_redirect'),
    path("accounts/", include('django.contrib.auth.urls')),
    path('task/', include(tasks_patterns)),
    path('stats/', views.stats),
    path('settings/', include(settings_patterns)),
    path('feedback/', views.feedback),
]
