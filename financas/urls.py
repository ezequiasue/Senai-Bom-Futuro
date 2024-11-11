from django.urls import path
from . import views  # Importa as views do seu arquivo views.py

urlpatterns = [
    path('', views.lista_transacoes, name='index'),  # A URL principal é a lista_transacoes
    path('relatorio/', views.relatorio_categoria, name='relatorio_categoria'),  # Relatório por categoria
]
