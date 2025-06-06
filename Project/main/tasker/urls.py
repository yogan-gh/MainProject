from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:id>", views.details),
    path("create/", views.details),
    path("edit/<int:id>/", views.details),
    path("delete/<int:id>/", views.details),
    path('stats', views.stats),
    path('settings', views.settings),
    path('feedback', views.feedback),
]
