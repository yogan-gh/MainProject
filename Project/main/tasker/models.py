from django.db import models
from django.contrib.auth.models import User

def get_default_status_id():
    return TaskStatus.objects.get_or_create(status='new')[0].id

def get_new_status():
    return TaskStatus.objects.get(status='new')
def get_process_status():
    return TaskStatus.objects.get(status='in_progress')
def get_review_status():
    return TaskStatus.objects.get(status='review')
def get_revision_status():
    return TaskStatus.objects.get(status='revision')
def get_complete_status():
    return TaskStatus.objects.get(status='complete')
def get_cancel_status():
    return TaskStatus.objects.get(status='cancel')

class CustomUser(User):
    class Meta:
        proxy = True
    def __str__(self):
        return f"{self.first_name} ({self.username})"

class TaskSubjects(models.Model):
    name = models.CharField()
    synonym = models.CharField()
    def __str__(self):
        return f"{self.synonym} ({self.name})"

class TaskStatus(models.Model):
    status = models.CharField()
    synonym = models.CharField()
    def __str__(self):
        return self.synonym

class InternetAccounts(models.Model):
    account = models.CharField()
    def __str__(self):
        return self.account

class Emails(models.Model):
    email = models.CharField()
    def __str__(self):
        return self.email

class PhoneNumbers(models.Model):
    numbers = models.CharField()
    def __str__(self):
        return self.numbers

class Persons(models.Model):
    person = models.CharField()
    def __str__(self):
        return self.person

class Tasks(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    subject = models.ForeignKey(TaskSubjects, on_delete=models.PROTECT)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, default=get_new_status)
    start_date = models.DateField()
    end_date = models.DateField()
    persons = models.ManyToManyField(Persons)
    phoneNumbers = models.ManyToManyField(PhoneNumbers)
    accounts = models.ManyToManyField(InternetAccounts)
    emails = models.ManyToManyField(Emails)

    file = models.FileField(upload_to='task_files/', blank=True, null=True, verbose_name="Прикрепленный файл")
    file_name = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.file and not self.file_name:
            self.file_name = self.file.name
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.file:
            self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Task to {self.user}"
