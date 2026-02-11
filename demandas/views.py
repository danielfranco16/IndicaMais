from ast import In
import re
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import login_required, prefeitura_required, vereador_required, camara_required
from django.core.paginator import Paginator
import demandas
from .models import Demanda, gerar_protocolo
from .forms import DemandaForm
from indicacoes.forms import IndicacoesForm

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    form = DemandaForm(request.POST)
    if request.method == 'POST':
        nova_demanda = form.save(commit=False)
        nova_demanda.protocolo = gerar_protocolo(nova_demanda.nome_autor)
        nova_demanda.save()
            
        return render(request, 'protocolo.html', {'form': form, 'demanda': nova_demanda})

    return render(request, 'registro_demandas.html', {'form': form})


def busca(request):
    protocolo = request.GET.get('protocolo')
    
    if protocolo: 
        demanda = Demanda.objects.filter(protocolo=protocolo).first()
        return render(request, 'busca.html', {'demanda': demanda})
    else:
        return render(request, 'busca.html')
    

@vereador_required
def exibir_demandas(request):

    demandas_list = Demanda.objects.all()
    paginator = Paginator(demandas_list, 3) # Apresenta  3 demandas por página
    page_number = request.GET.get('page')
    demandas = paginator.get_page(page_number)

    return render(request, 'exibir_demandas.html', {'demandas': demandas})   







