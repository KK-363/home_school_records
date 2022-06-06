from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *

class AddStudent(ModelForm):
    class Meta:
         model = Student
         fields = ('first_name', 'last_name', 'grade', 'age')

class AddSubject(ModelForm):
    class Meta:
         model = Subject
         fields = ('name', 'description', 'extra_curricular', 'student')         

    
class AddRecord(ModelForm):
    class Meta:
         model = Record
         fields = ('date', 'completed', 'time_spent', 'student', 'subject')
   

class GetRecordForm(forms.Form):   
    fname = forms.CharField(max_length=100)
    sname = forms.CharField(max_length=100)
    year = forms.CharField(max_length=10)
    month = forms.CharField(max_length=10)