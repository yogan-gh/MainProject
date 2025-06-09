from django.db import models

# Create your models here.
def get_default_status():
    return TaskStatus.objects.get_or_create(status='Зарегистрирован')[0].id

class Users(models.Model):
    user_number = models.IntegerField()
    abbreviation = models.CharField()
    def __str__(self):
        return str(self.user_number)

class TaskSubjects(models.Model):
    name = models.CharField()
    synonym = models.CharField()
    def __str__(self):
        return self.synonym

class TaskStatus(models.Model):
    status = models.CharField()
    def __str__(self):
        return self.status

class InternetAccounts(models.Model):
    url = models.CharField()
    def __str__(self):
        return self.url

class Emails(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class PhoneNumbers(models.Model):
    numbers = models.IntegerField()
    def __str__(self):
        return self.numbers

class Persons(models.Model):
    person = models.CharField()
    def __str__(self):
        return self.person

class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    subject = models.ForeignKey(TaskSubjects, on_delete=models.PROTECT)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, default=get_default_status)
    start_date = models.DateField()
    end_date = models.DateField()
    persons = models.ManyToManyField(Persons)
    internet_accounts = models.ManyToManyField(InternetAccounts)
    emails = models.ManyToManyField(Emails)
    phoneNumbers = models.ManyToManyField(PhoneNumbers)
    def __str__(self):
        return f"Task to {self.user}"
