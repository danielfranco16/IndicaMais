
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='lading'), # Rota para a página inicial do módulo demandas
    path('registro-demandas/', views.cadastro, name='registro_demandas'), # Rota para cadastro de demandas # name é o que vai ser usado no template
    path('busca/', views.busca, name='busca_protocolo'), # Rota para acompanhamento de demandas
    path('lista-demandas/', views.lista_demandas, name='lista_demandas'), # Rota para lista de demandas
    
]
