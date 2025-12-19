# qualidade/views/__init__.py
"""
Importa todas as views para manter compatibilidade com urls.py
"""

from .auth import *
from .fichas import *
from .partes import *
from .operadores import *
from .api import * 
from .relatorios import *
from .dashboard import *
from .inventario import *

__all__ = [
    # Auth
    'login_view',
    'logout_view',
    
    # Fichas
    'home',
    'criar_ficha',
    'editar_ficha',
    'visualizar_ficha',
    'excluir_ficha',
    'lixeira_fichas',
    
    # Partes
    'gerenciar_partes',
    'lixeira_partes',
    
    # Operadores
    'gerenciar_operadores',
    'lixeira_operadores',
    
    # API
    'adicionar_parte_ficha',
    'remover_parte_ficha',
    'adicionar_quantidade',
    'remover_quantidade',
    'api_cores_por_modelo',
    'api_tamanhos_por_modelo_e_cor',
    'api_remover_item',
    'api_atualizar_item',
    'api_adicionar_item_inventario',
    'get_cores',
    'get_tamanhos',
    
    # Relatórios
    'relatorios',
    'gerar_relatorio',
    'gerar_relatorio_periodo',
    
    # Dashboard
    'telas',

    #Inventário
    'criar_ficha_inventario',
    'editar_ficha_inventario',
    'get_cores_modelo',
    'get_tamanhos_modelo',
    'adicionar_item_inventario',
    'atualizar_quantidade_item',
    'remover_item_inventario',
]