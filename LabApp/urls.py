"""LabApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('LoginPage.urls', namespace='LoginPage')),
    path('homepage/', include('LoginPage.urls', namespace='homepage')),
    path('clientes/', include('AppClientes.urls', namespace='ClientesLab')),
    path('tipos-os/', include('AppTiposOs.urls', namespace='TipoOS_home')),
    path('ordens-servico/', include('AppOrdemServico.urls', namespace='ordens_servico')),
]
