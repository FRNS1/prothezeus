from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'AppClientes'

urlpatterns = [
    path('', ClientesLab, name='ClientesLab'),
    path('cadastro-cliente/', ClientesCad, name='ClientesCad'),
]
