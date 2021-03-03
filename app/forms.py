from django import forms
from app.models import Task
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from datetime import datetime

class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'

class TaskForm(forms.ModelForm):
    task_date=forms.DateTimeField(widget=DateTimeInput())
    due_date=forms.DateTimeField(widget=DateTimeInput())
    class Meta:
        model = Task
        fields = ("task",'description','task_date','due_date')
    
    def clean(self):
        cleaned_data=super().clean()
        present_time=timezone.now()
        if cleaned_data.get('task_date') <= present_time:
            raise forms.ValidationError('Task Not Schedule in Back Date',code='Invalid')
        if cleaned_data.get('task_date') >= cleaned_data.get('due_date'):
            raise forms.ValidationError('Due Date Must be Greater Than Start Date',code='Invalid')

class TaskUpdateForm(forms.ModelForm):
    task_date=forms.DateTimeField(widget=DateTimeInput())
    due_date=forms.DateTimeField(widget=DateTimeInput())
    class Meta:
        model = Task
        fields = ("task",'description','task_date','due_date')
    def clean(self):
        cleaned_data=super().clean()
        present_time=timezone.now()
        if cleaned_data.get('task_date') <= present_time:
            raise forms.ValidationError('Task Not Schedule in Back Date',code='Invalid')
        if cleaned_data.get('task_date') >= cleaned_data.get('due_date'):
            raise forms.ValidationError('Due Date Must be Greater Than Start Date',code='Invalid')