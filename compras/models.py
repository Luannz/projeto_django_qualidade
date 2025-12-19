from django.db import models
from django.contrib.auth.models import User

class Modelo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
    
    def __str__(self):
        return self.nome


class Cor(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
    
    def __str__(self):
        return self.nome

class Requisicao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Requisição'
        verbose_name_plural = 'Requisições'
    
    def __str__(self):
        return f"Requisição #{self.id} - {self.usuario.username} - {self.data_criacao.strftime('%d/%m/%Y')}"


class ItemRequisicao(models.Model):
    TAMANHOS = [(i, i) for i in range(26, 45)]
    requisicao = models.ForeignKey(Requisicao, on_delete=models.CASCADE, related_name='itens')
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    tamanho = models.PositiveSmallIntegerField(choices=TAMANHOS)
    quantidade = models.PositiveIntegerField()
    observacao = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Item da Requisição'
        verbose_name_plural = 'Itens da Requisição'
    
    def __str__(self):
        return f"{self.modelo} - {self.cor} - {self.tamanho} - Qtd: {self.quantidade}"