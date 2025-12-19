from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Requisicao, ItemRequisicao, Modelo, Cor
from .forms import ItemRequisicaoForm, RequisicaoForm, ModeloForm, CorForm
from .decorators import somente_loja

@login_required
@somente_loja
def home(request):
    """Lista todas as requisições do usuário logado"""
    requisicoes = Requisicao.objects.filter(usuario=request.user)
    return render(request, 'compras/home.html', {
        'requisicoes': requisicoes
    })


@login_required
@somente_loja
def nova_requisicao(request):
    """Cria uma nova requisição e redireciona para edição"""
    if request.method == 'POST':
        form = RequisicaoForm(request.POST)
        if form.is_valid():
            requisicao = form.save(commit=False)
            requisicao.usuario = request.user
            requisicao.save()
            messages.success(request, 'Requisição criada com sucesso!')
            return redirect('compras:editar_requisicao', requisicao_id=requisicao.id)
    else:
        form = RequisicaoForm()
    
    return render(request, 'compras/nova.html', {
        'form': form
    })


@login_required
@somente_loja
def editar_requisicao(request, requisicao_id):
    """Edita requisição e adiciona itens"""
    requisicao = get_object_or_404(Requisicao, id=requisicao_id, usuario=request.user)
    
    # Adicionar novo item
    if request.method == 'POST' and 'adicionar_item' in request.POST:
        form = ItemRequisicaoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.requisicao = requisicao
            item.save()
            messages.success(request, 'Item adicionado!')
            return redirect('compras:editar_requisicao', requisicao_id=requisicao.id)
    
    # Remover item
    elif request.method == 'POST' and 'remover_item' in request.POST:
        item_id = request.POST.get('item_id')
        ItemRequisicao.objects.filter(id=item_id, requisicao=requisicao).delete()
        messages.success(request, 'Item removido!')
        return redirect('compras:editar_requisicao', requisicao_id=requisicao.id)
    
    # Editar observação da requisição
    elif request.method == 'POST' and 'editar_observacao' in request.POST:
        form_req = RequisicaoForm(request.POST, instance=requisicao)
        if form_req.is_valid():
            form_req.save()
            messages.success(request, 'Observação atualizada!')
            return redirect('compras:editar_requisicao', requisicao_id=requisicao.id)
    
    form = ItemRequisicaoForm()
    form_req = RequisicaoForm(instance=requisicao)
    
    return render(request, 'compras/editar.html', {
        'requisicao': requisicao,
        'form': form,
        'form_req': form_req,
        'itens': requisicao.itens.all()
    })


# ==================== CADASTROS ====================

@login_required
@somente_loja
def cadastros(request):
    """Página principal de cadastros"""
    modelos = Modelo.objects.all()
    cores = Cor.objects.all()
    
    return render(request, 'compras/cadastros.html', {
        'modelos': modelos,
        'cores': cores
    })


@login_required
@somente_loja
def cadastrar_modelo(request):
    """Cadastra um novo modelo"""
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modelo cadastrado com sucesso!')
            return redirect('compras:cadastros')
    else:
        form = ModeloForm()
    
    return render(request, 'compras/cadastrar_modelo.html', {
        'form': form
    })


@login_required
@somente_loja
def editar_modelo(request, modelo_id):
    """Edita um modelo existente"""
    modelo = get_object_or_404(Modelo, id=modelo_id)
    
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modelo atualizado com sucesso!')
            return redirect('compras:cadastros')
    else:
        form = ModeloForm(instance=modelo)
    
    return render(request, 'compras/editar_modelo.html', {
        'form': form,
        'modelo': modelo
    })


@login_required
@somente_loja
def cadastrar_cor(request):
    """Cadastra uma nova cor"""
    if request.method == 'POST':
        form = CorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cor cadastrada com sucesso!')
            return redirect('compras:cadastros')
    else:
        form = CorForm()
    
    return render(request, 'compras/cadastrar_cor.html', {
        'form': form
    })


@login_required
@somente_loja
def editar_cor(request, cor_id):
    """Edita uma cor existente"""
    cor = get_object_or_404(Cor, id=cor_id)
    
    if request.method == 'POST':
        form = CorForm(request.POST, instance=cor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cor atualizada com sucesso!')
            return redirect('compras:cadastros')
    else:
        form = CorForm(instance=cor)
    
    return render(request, 'compras/editar_cor.html', {
        'form': form,
        'cor': cor
    })

