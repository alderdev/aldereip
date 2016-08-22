from django import forms
from django.forms import ModelForm, Textarea, CharField
from .models import WorkOrder


class WorkorderDetailForm(forms.ModelForm):
    model = WorkOrder
    exclude = ('create_at','modify' )
