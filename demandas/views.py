import re
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import login_required, prefeitura_required, vereador_required, camara_required
from .models import Demanda, gerar_protocolo
from .forms import DemandaForm

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    form = DemandaForm(request.POST)
    if request.method == 'POST':
        nova_demanda = form.save(commit=False)
        nova_demanda.protocolo = gerar_protocolo(nova_demanda.nome_autor)
        nova_demanda.save()
            
        return redirect('home')

    return render(request, 'registro_demandas.html', {'form': form})


def busca(request):
    protocolo = request.GET.get('protocolo')

    
    if protocolo: 
        demanda = get_object_or_404(Demanda, protocolo=protocolo)
        return render(request, 'busca.html', {'demanda': demanda})
    else:
        return render(request, 'busca.html')
    
    return render(request, 'tasks-list.html', {'tasks': tasks})



def acompanhamento_protocolo(request, protocolo):
    print(  protocolo  )
    demanda = get_object_or_404(Demanda, protocolo=protocolo)
    form = DemandaForm(instance=demanda)
    return render(request, 'acompanhamento.html', {'demanda': demanda})


@vereador_required
def lista_demandas(request):
    return render(request, 'lista_demandas.html')   