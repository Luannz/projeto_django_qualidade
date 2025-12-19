from django import forms
from .models import ItemRequisicao, Requisicao, Modelo, Cor

class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = ['observacao']
        widgets = {
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observações gerais (opcional)'
            })
        }


class ItemRequisicaoForm(forms.ModelForm):
    class Meta:
        model = ItemRequisicao
        fields = ['modelo', 'cor', 'tamanho', 'quantidade', 'observacao']
        widgets = {
            'modelo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cor': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tamanho': forms.Select(attrs={
                'class': 'form-select'
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Ex: 10'
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Observações do item (opcional)'
            })
        }
        labels = {
            'modelo': 'Modelo',
            'cor': 'Cor',
            'tamanho': 'Tamanho',
            'quantidade': 'Quantidade',
            'observacao': 'Observações'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas itens ativos
        self.fields['modelo'].queryset = self.fields['modelo'].queryset.filter(ativo=True)
        self.fields['cor'].queryset = self.fields['cor'].queryset.filter(ativo=True)


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Tênis Esportivo'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'nome': 'Nome do Modelo',
            'ativo': 'Ativo'
        }


class CorForm(forms.ModelForm):
    class Meta:
        model = Cor
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Preto'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'nome': 'Nome da Cor',
            'ativo': 'Ativo'
        }