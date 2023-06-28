from django import forms
from django.forms import widgets
from .models import Task


class TaskForms(forms.Form):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'start_date', 'date_of_completion']