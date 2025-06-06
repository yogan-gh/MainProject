from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:id>", views.detail),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path('stats', views.stats),
    path('settings', views.settings),
    path('feedback', views.feedback),
]
