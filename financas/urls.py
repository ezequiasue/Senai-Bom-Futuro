from django.urls import path
from . import views  # Importa as views do mesmo diretório

urlpatterns = [
    path('', views.index, name='index'),  # Mapeia a URL raiz para a view index
    #path('', views.lista_transacoes, name='lista_transacoes'),  # Mapeia a URL raiz para a view lista_transacoes
]