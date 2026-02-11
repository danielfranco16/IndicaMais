
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro_indicacao'), # Rota para cadastro de demandas # name é o que vai ser usado no template
    path('adotar-demandas/<int:id>/', views.adotar_demandas, name='adotar_demanda'), # Rota para adoção de demandas por vereadores



    path('detalhar/', views.detalhar, name='detalhar_indicacao'), # Rota para detalhar uma demanda específica
    path('lista-camara/', views.lista_camara, name='lista_indicacoes_camara'), # Rota para a página inicial do módulo demandas
    path('lista-prefeitura/', views.lista_prefeitura, name='lista_indicacoes_prefeitura'), # Rota para a página inicial do módulo demandas para prefeitura
    path('minhas-indicacoes/', views.lista_vereador, name='lista_indicacoes_vereador'), # Rota para a página inicial do módulo demandas para vereadores

]
