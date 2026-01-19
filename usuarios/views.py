from django.shortcuts import render
from core.decorators import login_required

# Create your views here.


##def lista(request):
##    return render(request, 'lista_usuarios.html')

@login_required
def perfil(request):        
    return render(request, 'perfil_usuario.html')