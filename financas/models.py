from django.db import models
from django.utils import timezone
from django.db.models import Sum

# Modelo para a Categoria de Transações
class Categorias(models.Model):
    # Atributo nome da categoria (campo de texto de até 100 caracteres)
    nome = models.CharField(max_length=100, unique=True)
    # Atributo descrição da categoria (campo de texto livre)
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        # Método __str__ define como o objeto será representado em texto
        return self.nome

    class Meta:
        # Definindo como o nome da categoria será exibido no plural e singular
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

# Modelo para a Transação
class Transacao(models.Model):
    # Definindo os tipos de transação possíveis: entrada ou saída
    TIPOS_TRANSACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída')
    ]
    
    # Atributo tipo da transação, baseado nas opções definidas acima
    tipo = models.CharField(max_length=7, choices=TIPOS_TRANSACAO)
    # Atributo valor da transação (campo numérico com até 10 dígitos, sendo 2 casas decimais)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    # Atributo categoria da transação, que é uma chave estrangeira referenciando a tabela Categorias
    categoria = models.ForeignKey('Categorias', on_delete=models.SET_NULL, null=True)
    # Atributo descrição da transação (campo de texto livre)
    descricao = models.TextField(blank=True, null=True)
    # Atributo data da transação (data e hora atual por padrão)
    data = models.DateTimeField(default=timezone.now)
    # Atributo para armazenar o saldo total após a transação (campo numérico)
    saldo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Atributo para indicar se a transação foi paga ou não (campo booleano)
    pago = models.BooleanField(default=False)
    # Atributo para armazenar a data de vencimento da transação (campo de data)
    data_vencimento = models.DateField(blank=True, null=True)

    def __str__(self):
        # Método __str__ define como o objeto será representado em texto
        return f"{self.get_tipo_display()} - {self.valor} em {self.data.strftime('%Y-%m-%d %H:%M:%S')}"

    @classmethod
    def calcular_saldo(cls):
        # Método de classe para calcular o saldo total (entrada - saída)
        # 'entrada' -> Soma dos valores de transações do tipo entrada
        entradas = cls.objects.filter(tipo='entrada').aggregate(total=Sum('valor'))['total'] or 0
        # 'saida' -> Soma dos valores de transações do tipo saída
        saidas = cls.objects.filter(tipo='saida').aggregate(total=Sum('valor'))['total'] or 0
        # Retorna o saldo total (entradas - saídas)
        return entradas - saidas

    class Meta:
        # Definindo como o nome da transação será exibido no plural e singular
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
