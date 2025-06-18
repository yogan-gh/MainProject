from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_default_status():
    return TaskStatus.objects.get_or_create(status='new')[0].id
def get_process_status():
    return TaskStatus.objects.get_or_create(status='in_progress')[0].id

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
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, default=get_default_status)
    start_date = models.DateField()
    end_date = models.DateField()
    persons = models.ManyToManyField(Persons)
    phoneNumbers = models.ManyToManyField(PhoneNumbers)
    accounts = models.ManyToManyField(InternetAccounts)
    emails = models.ManyToManyField(Emails)
    def __str__(self):
        return f"Task to {self.user}"
