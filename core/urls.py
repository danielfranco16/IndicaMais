
from django.contrib import admin
from django.urls import include, path
from . import views
##from aplicativos import usuarios, demandas, legislativo, executivo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demandas.urls')), # Rota modulo demandas cidadãos 
    path('indicacoes/', include('indicacoes.urls')), # Rota modulo indicacoes
    path('legislativo/', include('legislativo.urls')), # Rota modulo legislativo
    path('executivo/', include('executivo.urls')), # Rota modulo executivo
    path('accounts/', include('django.contrib.auth.urls')), # Rota para login, logout, password change, password reset
    path('redirect/', views.home_index, name='home'),
    path('usuarios/', include('usuarios.urls')), # Rota modulo usuarios
]
