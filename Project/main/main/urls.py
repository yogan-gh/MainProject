from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasker/', include('tasker.urls')),
    path('', RedirectView.as_view(url='/tasker/', permanent=True)),
]
