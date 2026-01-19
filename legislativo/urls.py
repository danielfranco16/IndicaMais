
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from . import views

urlpatterns = [
    path('home-camara/', views.home_camara, name='home_camara'), # Rota para a página inicial do módulo legislativo
    path('home-vereador/', views.home_vereador, name='home_vereador'), # Rota

]
