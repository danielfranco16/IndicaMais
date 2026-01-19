from django.shortcuts import render
from core.decorators import login_required, prefeitura_required, vereador_required, camara_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'registro_demandas.html')


def acompanhamento(request):
    return render(request, 'acompanhamento.html')

@vereador_required
def lista_demandas(request):
    return render(request, 'lista_demandas.html')   