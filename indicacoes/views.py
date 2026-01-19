from django.shortcuts import render
from core.decorators import login_required, prefeitura_required, vereador_required, camara_required

@vereador_required
def cadastro(request):
    return render(request, 'cadastro_indicacao.html')

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



