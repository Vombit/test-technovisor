from django import forms
from .models import *


class OrderForm(forms.Form):
    staffer = forms.ModelChoiceField(
        queryset=Staffer.objects.all(),
        label='Выбор сотрудника',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    date = forms.DateField(
        label='Выбор даты',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        label='Выбор блюд',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )