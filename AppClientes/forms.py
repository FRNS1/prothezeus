from django import forms

from .models import *


class CadastrarCliente(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
