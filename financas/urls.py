# Importa as views definidas no arquivo views.py
from django.urls import path
from . import views

# Define o conjunto de URLs que serão mapeadas para as funções das views
urlpatterns = [
    # URL para a página principal que lista todas as transações
    path('', views.lista_transacoes, name='index'),
    # URL para exibir o relatório de transações agrupadas por categoria
    path('relatorio/', views.relatorio_categoria, name='relatorio_categoria'),
    # URL para lançar uma nova transação
    path('lancar/', views.lancar_transacao, name='lancar_transacao'),
    # URL para cadastrar uma nova categoria
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),  # Nova URL para cadastrar categoria
]
