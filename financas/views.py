from django.shortcuts import render
from .models import Transacao, Categorias
from django.db.models import Sum  # Certifique-se de importar o Sum

def resumo_por_categoria():
    # Consulta o total por categoria
    return Transacao.objects.values('categoria__nome').annotate(
        total=Sum('valor')
    ).order_by('categoria__nome')

def lista_transacoes(request):
    transacoes = Transacao.objects.all()  # Busca todas as transações
    categorias = Categorias.objects.all()   # Busca todas as categorias
    resumo = resumo_por_categoria()  # Obtém o resumo por categoria
    return render(request, 'index.html', {'transacoes': transacoes, 'categorias': categorias, 'resumo': resumo})


def relatorio_categoria(request):
    """
    Exibe um relatório de transações agrupadas por categoria.
    """
    resumo = resumo_por_categoria()
    return render(request, 'relatorio_categoria.html', {'resumo': resumo})
