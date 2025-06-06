from django.contrib import admin
from django.urls import path
from tasker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path('stats', views.stats),
    path('settings', views.settings),
    path('feedback', views.feedback),
    path('task-details', views.details),
]
