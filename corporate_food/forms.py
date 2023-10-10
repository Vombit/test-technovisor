from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['staffer', 'date']
        labels = {
            'staffer': 'Cотрудник',
            'date': 'Дата',
        }
        widgets = {
            'staffer': forms.RadioSelect,
            'date': forms.DateInput(attrs={'type': 'date', 'id': "date"}),
        }