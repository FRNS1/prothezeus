import django_filters

from .models import *


class FilterClientes(django_filters.FilterSet):

    class Meta:
        model = clientes
        fields = {
            'nome_completo': ['icontains'],
            'telefone': ['icontains'],
            'email': ['icontains'],
            'endereco': ['icontains'],
            'preco': ['icontains'],
            }