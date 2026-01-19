
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from usuarios import views
##from aplicativos import usuarios, demandas, legislativo, executivo

urlpatterns = [
    ##path('lista/',views.lista, name='lista_usuarios'),
    path('perfil/',views.perfil, name='perfil_usuario'),

]
