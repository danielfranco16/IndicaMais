from django.shortcuts import render
from core.decorators import prefeitura_required

@prefeitura_required
def home_prefeitura(request):
    return render(request, 'home_prefeitura.html')

