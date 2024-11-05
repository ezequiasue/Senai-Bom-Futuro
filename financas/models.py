# financas/models.py

from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    """
    Modelo para armazenar categorias de receitas e despesas, como "Alimentação", "Salário", "Transporte", etc.
    """
    nome = models.CharField(max_length=100, unique=True)  # Nome da categoria
    descricao = models.TextField(blank=True, null=True)   # Descrição opcional

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"  # Nome plural para o painel admin


class Transacao(models.Model):
    """
    Modelo para armazenar as transações financeiras, tanto receitas quanto despesas.
    """
    TIPOS_TRANSACAO = [
        ('entrada', 'Entrada'),    # Para receitas
        ('saida', 'Saída')         # Para despesas
    ]

    tipo = models.CharField(max_length=7, choices=TIPOS_TRANSACAO)  # Se é uma receita ou despesa
    valor = models.DecimalField(max_digits=10, decimal_places=2)    # Valor da transação
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)  # Categoria da transação
    descricao = models.TextField(blank=True, null=True)  # Descrição opcional da transação
    data = models.DateTimeField(default=timezone.now)    # Data e hora da transação
    saldo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Saldo após a transação

    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.valor} - {self.categoria.nome if self.categoria else 'Sem Categoria'}"

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"  # Nome plural para o painel admin
