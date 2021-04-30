from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Employee, Order
from django.core import validators

from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        exclude=['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['number_naryad', 'technical_activities', 'place_name_work', 'work_supervisor', 'team_members', 'person_give_naryad', 'started_work', 'work_done']
        widgets = {
            'number_naryad': widgets.NumberInput(attrs={'class':'form-control'}),
            'technical_activities': widgets.TextInput(attrs={'class':'form-control'}),
            'place_name_work': widgets.TextInput(attrs={'class':'form-control'}),
            'work_supervisor': widgets.Select(attrs={'class':'form-control select2'}),
            'team_members': widgets.SelectMultiple(attrs={'class':"form-control select2 selectpicker", 'multiple data-live-search':"true"}),
            'person_give_naryad': widgets.Select(attrs={'class':'form-control select2'}),
            'started_work': widgets.DateInput(attrs={'class':'form-control','id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'work_done':  widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"})

        }

