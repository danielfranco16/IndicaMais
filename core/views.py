from django.shortcuts import render, redirect


def home_index(request):
    user = request.user

    # 1. Superusuário (Admin)
    #if user.is_superuser:
        #return redirect('/admin')

    # 2. Vereadores
    if user.groups.filter(name='vereador').exists():
        # Certifique-se que o name='dashboard_vereador' existe no seu urls.py
        return redirect('home_vereador')

    # 3. Funcionários da Câmara
    if user.groups.filter(name='funcionario_camara').exists():
        return redirect('home_camara')
    # 4. Funcionários da Prefeitura
    if user.groups.filter(name='funcionario_prefeitura').exists():
        return redirect('home_prefeitura')

    # 5. Cidadão (ou fallback se não tiver grupo)
    # Redireciona para a home pública ou painel do cidadão
    return redirect('lading')  # Certifique-se que o name='landing' existe no seu urls.py