from django import forms

from .models import *


class CadastrarServico(forms.ModelForm):
    class Meta:
        model = tipoos
        fields = '__all__'
