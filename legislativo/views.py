from django.shortcuts import render
from core.decorators import vereador_required , camara_required
from indicacoes.models import Indicacoes
from django.core.paginator import Paginator

# Create your views here.
@camara_required
def home_camara(request):
    return render(request, 'home_camara.html')


@vereador_required
def home_vereador(request):

    indicacoes_list = Indicacoes.objects.filter(nome_vereador=request.user).order_by('-data_cadastro')  # Ordena as indicações do mais recente para o mais antigo
    paginator = Paginator(indicacoes_list, 3)  # Apresenta 3 indicações por página
    page_number = request.GET.get('page')
    indicacoes = paginator.get_page(page_number)   
    total_indicacoes = Indicacoes.objects.filter(nome_vereador=request.user).count()  # Contagem total de indicações por verador 
    total_em_analise = Indicacoes.objects.filter(nome_vereador=request.user, status='em_analise').count()  
    total_aprovadas = Indicacoes.objects.filter(nome_vereador=request.user, status='aprovada').count()
    total_concluidas = Indicacoes.objects.filter(nome_vereador=request.user, status='concluida').count()

    return render(request, 'home_vereador.html', {'indicacoes': indicacoes, 
                                                  'total_indicacoes': total_indicacoes,
                                                  'total_em_analise': total_em_analise, 
                                                  'total_aprovadas': total_aprovadas, 
                                                  'total_concluidas': total_concluidas})

 