from ast import In
from re import I
from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import login_required, prefeitura_required, vereador_required, camara_required
from demandas.models import Demanda
from demandas.forms import DemandaForm
from .forms import IndicacoesForm

@vereador_required
def cadastro(request):
    form = IndicacoesForm(request.POST)
    if request.method == 'POST':
        nova_indicacao = form.save(commit=False)
        nova_indicacao.nome_vereador = request.user 
        nova_indicacao.save()
            
        return render(request, 'home.html')

    return render(request, 'cadastro_indicacao.html', {'form': form})



@vereador_required
def adotar_demandas(request, id):

 # Pega a demanda ou retorna 404 se não existir
    demanda = get_object_or_404(Demanda, id=id)

    if request.method == 'POST':

        form = IndicacoesForm(request.POST)
        
        if form.is_valid():
            nova_indicacao = form.save(commit=False)
            nova_indicacao.nome_vereador = request.user 
            nova_indicacao.save()

            print("Demanda adotada com sucesso!")
            return redirect('home')  # ou outra página de confirmação
    else:
        # Formulário preenchido com os dados da demanda
        form = IndicacoesForm(instance=demanda) 

    return render(request, 'adotar_demanda.html', {'form': form})

    

@login_required
def detalhar(request):
## def detalhar(request, indicacao_id):  # Caso queira detalhar uma indicação específica
    return render(request, 'detalhar_indicacao.html')

@camara_required
def lista_camara(request):
    return render(request, 'lista_indicacoes_camara.html')

@prefeitura_required
def lista_prefeitura(request):
    return render(request, 'lista_indicacoes_prefeitura.html')


@vereador_required
def lista_vereador(request):
    return render(request, 'lista_indicacoes_vereador.html')



