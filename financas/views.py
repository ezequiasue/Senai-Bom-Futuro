from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 
    
    
    
""" from django.shortcuts import render
from .models import Transacao, Categoria

def lista_transacoes(request):
    transacoes = Transacao.objects.all()  # Busca todas as transações
    categorias = Categoria.objects.all()   # Busca todas as categorias
    return render(request, 'home.html', {'transacoes': transacoes, 'categorias': categorias}) """