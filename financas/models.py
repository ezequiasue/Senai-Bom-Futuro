# financas/models.py
from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Categorias(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Transacao(models.Model):
    TIPOS_TRANSACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saida')
    ]
    tipo = models.CharField(max_length=7, choices=TIPOS_TRANSACAO)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categorias', on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)
    saldo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pago = models.BooleanField(default=False)
    data_vencimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.valor} em {self.data.strftime('%Y-%m-%d %H:%M:%S')}"

    @classmethod
    def calcular_saldo(cls):
        entradas = cls.objects.filter(tipo='entrada').aggregate(total=Sum('valor'))['total'] or 0
        saidas = cls.objects.filter(tipo='saida').aggregate(total=Sum('valor'))['total'] or 0
        return entradas - saidas

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transacões"

