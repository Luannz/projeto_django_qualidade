from django.contrib import admin
from .models import (Modelo,Cor,Requisicao,ItemRequisicao)


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo', 'data_cadastro']
    list_filter = ['ativo']
    search_fields = ['nome']
    ordering = ['nome']


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo', 'data_cadastro']
    list_filter = ['ativo']
    search_fields = ['nome']
    ordering = ['nome']

class ItemRequisicaoInline(admin.TabularInline):
    model = ItemRequisicao
    extra = 1
    fields = ['modelo', 'cor', 'tamanho', 'quantidade', 'observacao']


@admin.register(Requisicao)
class RequisicaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'data_criacao', 'total_itens']
    list_filter = ['data_criacao', 'usuario']
    search_fields = ['usuario__username', 'observacao']
    date_hierarchy = 'data_criacao'
    inlines = [ItemRequisicaoInline]

    def total_itens(self, obj):
        return obj.itens.count()

    total_itens.short_description = 'Total de Itens'


@admin.register(ItemRequisicao)
class ItemRequisicaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'requisicao', 'modelo', 'cor', 'tamanho', 'quantidade']
    list_filter = ['modelo', 'cor', 'tamanho']
    search_fields = ['requisicao__id', 'modelo__nome', 'cor__nome']
