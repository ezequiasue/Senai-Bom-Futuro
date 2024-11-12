from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transacao, Categorias

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

from django.shortcuts import render, redirect
from .models import Categorias
from django.http import HttpResponse

def cadastrar_categoria(request):
    """
    View para cadastrar uma nova categoria.
    """
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        # Verifica se o nome foi fornecido e cria a categoria
        if nome:
            categoria = Categorias(nome=nome, descricao=descricao)
            categoria.save()
            return redirect('index')  # Redireciona para a página principal (ajuste conforme necessário)
        else:
            return HttpResponse("Erro: O nome da categoria é obrigatório.", status=400)

    return render(request, 'cadastrar_categoria.html')  # Renderiza a página de cadastro


def lancar_transacao(request):
    """
    View para criar uma nova transação.
    """
    categorias = Categorias.objects.all()  # Busca todas as categorias para exibir no formulário

    if request.method == 'POST':
        # Obtem os dados do formulário manualmente
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        categoria_id = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        pago = request.POST.get('pago') == 'on'  # Checkbox será 'True' se marcado
        data_vencimento = request.POST.get('data_vencimento')

        # Validação simples dos campos obrigatórios
        if tipo and valor and categoria_id and data:
            categoria = Categorias.objects.get(id=categoria_id) if categoria_id else None
            transacao = Transacao(
                tipo=tipo,
                valor=valor,
                categoria=categoria,
                descricao=descricao,
                data=data,
                pago=pago,
                data_vencimento=data_vencimento
            )
            transacao.save()
            return redirect('index')  # Alterado para 'index' que é o nome da URL
        else:
            # Adicione uma mensagem de erro caso necessário
            error_message = "Por favor, preencha todos os campos obrigatórios."

            return render(request, 'lancar_transacao.html', {
                'categorias': categorias,
                'error_message': error_message
            })

    return render(request, 'lancar_transacao.html', {'categorias': categorias})
