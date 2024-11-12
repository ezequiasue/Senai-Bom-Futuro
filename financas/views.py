# Importações necessárias para as views
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transacao, Categorias  # Importa os modelos de Transacao e Categorias do banco de dados

# Função para calcular o resumo das transações por categoria
def resumo_por_categoria():
    """
    Função que retorna um resumo das transações agrupadas por categoria,
    incluindo o total de valores para cada categoria.
    """
    return Transacao.objects.values('categoria__nome').annotate(
        total=Sum('valor')  # Calcula o total de transações por categoria
    ).order_by('categoria__nome')  # Ordena o resultado pelo nome da categoria

# Função para exibir a lista de transações e o resumo por categoria
def lista_transacoes(request):
    """
    Função que exibe todas as transações e o resumo das transações por categoria.
    """
    transacoes = Transacao.objects.all()  # Busca todas as transações do banco de dados
    categorias = Categorias.objects.all()  # Busca todas as categorias do banco de dados
    resumo = resumo_por_categoria()  # Chama a função que retorna o resumo por categoria
    # Renderiza a página 'index.html' passando as transações, categorias e resumo
    return render(request, 'index.html', {'transacoes': transacoes, 'categorias': categorias, 'resumo': resumo})

# Função para exibir o relatório de transações agrupadas por categoria
def relatorio_categoria(request):
    """
    Exibe um relatório de transações agrupadas por categoria.
    """
    resumo = resumo_por_categoria()  # Obtém o resumo por categoria
    # Renderiza a página 'relatorio_categoria.html' passando o resumo como contexto
    return render(request, 'relatorio_categoria.html', {'resumo': resumo})

# Funções para cadastrar categorias e transações
from django.shortcuts import render, redirect
from .models import Categorias
from django.http import HttpResponse

# Função para cadastrar uma nova categoria
def cadastrar_categoria(request):
    """
    Função que permite ao usuário cadastrar uma nova categoria.
    """
    if request.method == 'POST':  # Verifica se o formulário foi enviado
        nome = request.POST.get('nome')  # Obtém o nome da categoria enviado pelo formulário
        descricao = request.POST.get('descricao')  # Obtém a descrição da categoria

        # Verifica se o nome foi informado, se sim, cria e salva a categoria
        if nome:
            categoria = Categorias(nome=nome, descricao=descricao)
            categoria.save()
            return redirect('index')  # Redireciona para a página principal após salvar a categoria
        else:
            # Se o nome não for informado, retorna uma mensagem de erro
            return HttpResponse("Erro: O nome da categoria é obrigatório.", status=400)

    # Se o método não for POST, renderiza a página de cadastro de categoria
    return render(request, 'cadastrar_categoria.html')

# Função para lançar uma nova transação
def lancar_transacao(request):
    """
    Função para criar uma nova transação.
    """
    categorias = Categorias.objects.all()  # Obtém todas as categorias para exibir no formulário

    if request.method == 'POST':  # Verifica se o formulário foi enviado
        # Obtém os dados enviados pelo formulário
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        categoria_id = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        pago = request.POST.get('pago') == 'on'  # Verifica se o checkbox foi marcado (True ou False)
        data_vencimento = request.POST.get('data_vencimento')

        # Valida se os campos obrigatórios foram preenchidos
        if tipo and valor and categoria_id and data:
            categoria = Categorias.objects.get(id=categoria_id) if categoria_id else None  # Obtém a categoria associada à transação
            # Cria a transação com os dados fornecidos
            transacao = Transacao(
                tipo=tipo,
                valor=valor,
                categoria=categoria,
                descricao=descricao,
                data=data,
                pago=pago,
                data_vencimento=data_vencimento
            )
            transacao.save()  # Salva a transação no banco de dados
            return redirect('index')  # Redireciona para a página principal após salvar a transação
        else:
            # Se faltar algum campo obrigatório, exibe uma mensagem de erro
            error_message = "Por favor, preencha todos os campos obrigatórios."
            # Renderiza a página de lançamento de transação com a mensagem de erro
            return render(request, 'lancar_transacao.html', {
                'categorias': categorias,
                'error_message': error_message
            })

    # Se o método não for POST, renderiza o formulário de lançamento de transação
    return render(request, 'lancar_transacao.html', {'categorias': categorias})
