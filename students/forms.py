# encoding: utf-8
from django import forms
from django.db import models

from students.models import Student
from django.forms.extras.widgets import SelectDateWidget



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        BIRTH_YEAR_CHOICES = tuple(range(1900,2001))
        widgets = {
            'date_of_birth': SelectDateWidget(years=BIRTH_YEAR_CHOICES)
        }



