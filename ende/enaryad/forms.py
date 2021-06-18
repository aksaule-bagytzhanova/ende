from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Employee, Order, create_e_naryad_table_1
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
            'work_supervisor': widgets.Select(attrs={'class':'form-control select2', 'style':'width: 100%;'}),
            'team_members': widgets.SelectMultiple(attrs={'class':"form-control select2 selectpicker", 'multiple data-live-search':"true"}),
            'person_give_naryad': widgets.Select(attrs={'class':'form-control select2'}),
            'started_work': widgets.DateInput(attrs={'class':'form-control','id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'work_done':  widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"})

        }

class CreateNar1Form(ModelForm):
    class Meta:
        model = create_e_naryad_table_1
        fields = ['organization', 'plot', 'admitting', 'team_members', 'category_of_work', 'emergency_preparedness_time', 'object', 'finish_work', 'name_electrical', 'separate_instructions', 'signature', 'subdivision', 'work_manager', 'manufacturer', 'observer', 'single_line_diagram', 'entrusted', 'start_work', 'disconnected_where', 'enar_give', 'biot_engineer', 'deputy_head']
        widgets = {
            'organization': widgets.Select(attrs={'class':'form-control select2'}),
            'plot': widgets.Select(attrs={'class':'form-control select2'}),
            'admitting': widgets.Select(attrs={'class':'form-control select2'}),
            'team_members': widgets.SelectMultiple(attrs={'class':"form-control select2 selectpicker", 'multiple data-live-search':"true"}),
            'category_of_work': widgets.Select(attrs={'class':'form-control select2'}),
            'emergency_preparedness_time': widgets.DateInput(attrs={'class':'form-control','id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'object': widgets.Select(attrs={'class':'form-control select2'}),
            'finish_work':  widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'name_electrical':widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 60px; width: 100%;'}),
            'separate_instructions': widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 60px; width: 100%;'}),
            'signature': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'subdivision': widgets.Select(attrs={'class':'form-control select2'}),
            'work_manager': widgets.Select(attrs={'class':'form-control select2'}),
            'manufacturer': widgets.Select(attrs={'class':'form-control select2'}),
            'observer': widgets.Select(attrs={'class':'form-control select2'}),
            'single_line_diagram': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'entrusted': widgets.Select(attrs={'class':'form-control select2'}),
            'start_work': widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'disconnected_where': widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 60px; width: 100%;'}),
            'enar_give': widgets.Select(attrs={'class':'form-control select2'}),
            'biot_engineer':widgets.Select(attrs={'class':'form-control select2'}),
            'deputy_head':widgets.Select(attrs={'class':'form-control select2'}),

        }

    def __init__(self, *args, **kwargs):
        super(CreateNar1Form, self).__init__(*args, **kwargs)
        self.fields['organization'].empty_label = "--- Выберите значение ---"
        self.fields['plot'].empty_label = "--- Выберите значение ---"
        self.fields['admitting'].empty_label = "--- Выберите значение ---"
        self.fields['category_of_work'].empty_label = "--- Выберите значение ---"
        self.fields['object'].empty_label = "--- Выберите значение ---"
        self.fields['subdivision'].empty_label = "--- Выберите значение ---"
        self.fields['work_manager'].empty_label = "--- Выберите значение ---"
        self.fields['manufacturer'].empty_label = "--- Выберите значение ---"
        self.fields['observer'].empty_label = "--- Выберите значение ---"
        self.fields['entrusted'].empty_label = "--- Выберите значение ---"
        self.fields['biot_engineer'].empty_label = "--- Выберите значение ---"
        self.fields['deputy_head'].empty_label = "--- Выберите значение ---"
