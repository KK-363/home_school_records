from django.db import models
from django.utils import timezone
import datetime

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        name = self.first_name + " " + self.last_name
        return name

    class Meta:
        ordering = ['last_name', 'first_name']


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=False, default='')
    extra_curricular = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Record(models.Model):
    date = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)
    time_spent = models.DecimalField(max_digits=10, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):        
        return str(self.date)

    class Meta:
        ordering = ['date']
        unique_together = [['student', 'subject', 'date']]


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField()
    event_length = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=False, default='')
    student = models.ManyToManyField(Student)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
