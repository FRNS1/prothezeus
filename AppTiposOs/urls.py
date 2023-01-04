from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'AppTiposOs'

urlpatterns = [
    path('', TipoOS_home, name='TipoOS_home'),
]
