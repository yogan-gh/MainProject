# Generated by Django 5.2.1 on 2025-06-21 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0017_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='task_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])], verbose_name='Прикрепленный файл'),
        ),
    ]
