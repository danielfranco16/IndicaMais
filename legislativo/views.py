from django.shortcuts import render
from core.decorators import vereador_required , camara_required

# Create your views here.
@camara_required
def home_camara(request):
    return render(request, 'home_camara.html')


@vereador_required
def home_vereador(request):
    return render(request, 'home_vereador.html')