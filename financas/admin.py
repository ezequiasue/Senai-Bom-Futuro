# financas/admin.py

from django.contrib import admin
from .models import Categoria, Transacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Campos a serem exibidos na lista
    search_fields = ('nome',)              # Campo de busca

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor', 'categoria', 'data', 'saldo_total')  # Campos a serem exibidos na lista
    list_filter = ('tipo', 'categoria', 'data')  # Filtros para o admin
    search_fields = ('descricao',)      # Campo de busca
    date_hierarchy = 'data'             # Permite filtrar por data
