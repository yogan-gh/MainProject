from django.db import models

# Create your models here.

class Users(models.Model):
    user_number = models.CharField()
    abbreviation = models.CharField()

class TaskSubjects(models.Model):
    name = models.CharField()
    synonym = models.CharField()

class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    subject = models.ForeignKey(TaskSubjects, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

class TaskInternetAccounts(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    internet_account = models.CharField()

class TaskEmails(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    email = models.EmailField()

class TaskPhoneNumbers(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    phone = models.IntegerField()

class TaskPersons(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    person = models.CharField()
    def __str__(self):
        return self.person
