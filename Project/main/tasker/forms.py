from django.forms import ModelForm
from .models import Tasks

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "user",
            "subject",
            "status",
            "start_date",
            "end_date",
        ]