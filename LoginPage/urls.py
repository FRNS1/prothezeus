from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'LoginPage'

urlpatterns = [
    path('', LoginPage, name='LoginPage'),
    path('homepage/', homepage, name='homepage'),
]
