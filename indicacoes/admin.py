from re import I
from django.contrib import admin

# Register your models here.
from .models import Indicacoes


@admin.register(Indicacoes)
class IndicacoesAdmin(admin.ModelAdmin):
    # Campos que aparecem na lista de usuários
    list_display = ('titulo', 'nome_vereador', 'categoria', 'urgencia', 'data_cadastro', 'status', 'id_demanda')