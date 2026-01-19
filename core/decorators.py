from django.shortcuts import redirect
from django.contrib import messages



def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# ==========================================
# DECORATOR: VEREADOR
# ==========================================
def vereador_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # 1. Verifica se está logado
        if not request.user.is_authenticated:
            return redirect('login') # ou redirecione para 'home' se preferir

        # 2. Verifica se pertence ao grupo 'vereador'
        # DICA: O nome do grupo no Django Admin deve ser EXATAMENTE 'vereador'
        if request.user.groups.filter(name='vereador').exists():
            return view_func(request, *args, **kwargs)
        
        # 3. Se falhar, avisa e redireciona para a Home
        messages.error(request, "Acesso negado. Área restrita a Vereadores.")
        return redirect('home')
        
    return _wrapped_view


# ==========================================
# DECORATOR: CÂMARA (Legislativo)
# ==========================================
def camara_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        # Verifica grupo 'funcionario_camara'
        if request.user.groups.filter(name='funcionario_camara').exists():
            return view_func(request, *args, **kwargs)
            
        messages.error(request, "Acesso negado. Área restrita à Câmara.")
        return redirect('home')

    return _wrapped_view


# ==========================================
# DECORATOR: PREFEITURA (Executivo)
# ==========================================
def prefeitura_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        # Verifica grupo 'funcionario_prefeitura'
        if request.user.groups.filter(name='funcionario_prefeitura').exists():
            return view_func(request, *args, **kwargs)

        messages.error(request, "Acesso negado. Área restrita à Prefeitura.")
        return redirect('home')

    return _wrapped_view