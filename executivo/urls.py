from django.shortcuts import render
from django.urls import include, path
from . import views

urlpatterns = [
    path('home-prefeitura/', views.home_prefeitura, name='home_prefeitura'), 
    #path('cadastro/', views.cadastro, name='cadastro-indicacoes'), # Rota para cadastro de demandas # name é o que vai ser usado no template
    #path('lista/', views.lista, name='lista-indicacoes'), # Rota para a página inicial do módulo demandas
]
    