from ast import In
from datetime import datetime
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import login_required, prefeitura_required, vereador_required, camara_required
from django.core.paginator import Paginator
import demandas
from .models import Demanda, gerar_protocolo
from .forms import DemandaForm

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    form = DemandaForm(request.POST)
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            nova_demanda = form.save(commit=False)
            nova_demanda.protocolo
            
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

    total_disponivel = Demanda.objects.filter(status='cadastrada').count()
    total_urgencia_alta = Demanda.objects.filter(status='cadastrada', urgencia='alta').count()
    total_urgencia_critica = Demanda.objects.filter(status='cadastrada', urgencia='critica').count()
    total_hoje = Demanda.objects.filter(data_cadastro__date = datetime.now().date()) 


    return render(request, 'exibir_demandas.html', {'demandas': demandas, 'total_disponivel': total_disponivel, 'total_urgencia_alta': total_urgencia_alta, 'total_urgencia_critica': total_urgencia_critica, 'total_hoje': total_hoje})   







