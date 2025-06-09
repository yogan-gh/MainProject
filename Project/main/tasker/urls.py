from django.urls import path, include
from . import views
from . import viewsSettings

settings_patterns = [
    # Users CRUD
    path('users/', viewsSettings.users_view, name='users_view'),
    path('add_user/', viewsSettings.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', viewsSettings.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', viewsSettings.delete_user, name='delete_user'),

    # TaskSubjects CRUD
    path('subjects/', viewsSettings.subjects_view, name='subjects_view'),
    path('add_subject/', viewsSettings.add_subject, name='add_subject'),
    path('edit_subject/<int:subject_id>/', viewsSettings.edit_subject, name='edit_subject'),
    path('delete_subject/<int:subject_id>/', viewsSettings.delete_subject, name='delete_subject'),

    # TaskStatus CRUD
    path('statuses/', viewsSettings.statuses_view, name='statuses_view'),
    path('add_status/', viewsSettings.add_status, name='add_status'),
    path('edit_status/<int:status_id>/', viewsSettings.edit_status, name='edit_status'),
    path('delete_status/<int:status_id>/', viewsSettings.delete_status, name='delete_status'),

    # Главная страница со всеми данными
    path('', viewsSettings.all_data_view, name='all_data'),
]

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.detail),
    path("create/", views.create),
    path('create/<int:id>/adddata/', views.adddata),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path('stats', views.stats),
    path('settings/', include(settings_patterns)),
    path('feedback', views.feedback),
]
