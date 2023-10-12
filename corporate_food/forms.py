from django import forms
from .models import *




class DishChoiceWidget(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        if value is None:
            option_value = ''
        return super().create_option(name, value, label, selected, index, subindex, attrs)




class DishChoiceWidget(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        if value is None:
            option_value = ''
        return super().create_option(name, value, label, selected, index, subindex, attrs)


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
        widget=DishChoiceWidget,
    )
    
    luck_me = forms.BooleanField(
        required=False,
        label='Добавить случайное блюдо'
    )