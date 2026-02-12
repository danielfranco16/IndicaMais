from django.contrib import admin

# Register your models here.
from .models import Demanda

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    # Campos que aparecem na lista de usuários
    list_display = ('id', 'titulo', 'nome_autor', 'categoria', 'urgencia', 'data_cadastro', 'status')