from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'AppOrdemServico'

urlpatterns = [
    path('', ordens_servico, name='ordens_servico'),
]
