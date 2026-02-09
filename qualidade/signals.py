from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
from django.apps import apps # Importante para verificar se o model existe

# removi o "from .models import PerfilUsuario" do topo para evitar importação precoce
# importar dentro da função para garantir que o Django já carregou tudo.

GRUPOS_PADRAO = ['Qualidade', 'Corte', 'Injetora',]

USUARIOS_PADRAO = [
    {'username': 'Qualidade01', 'password': 'lynd1234', 'grupo': 'Qualidade'},
    {'username': 'Operador01', 'password': 'lynd1234', 'grupo': 'Corte'},
    {'username': 'Injetora01', 'password': 'lynd1234', 'grupo': 'Injetora'},
]

@receiver(post_migrate)
def criar_dados_iniciais(sender, **kwargs):
    # 1. Só executa se o app que terminou a migração for o 'qualidade'
    if sender.name != 'qualidade':
        return

    # 2. Importação local para evitar erros de carregamento
    try:
        PerfilUsuario = apps.get_model('qualidade', 'PerfilUsuario')
    except LookupError:
        return

    print("Iniciando criação de dados padrões...")

    # 🔹 Criar grupos
    for nome_grupo in GRUPOS_PADRAO:
        Group.objects.get_or_create(name=nome_grupo)

    # 🔹 Criar usuários e perfis
    for user_data in USUARIOS_PADRAO:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'password': make_password(user_data['password']),
                'is_active': True
            }
        )

        # 🔹 Adicionar ao grupo
        grupo = Group.objects.get(name=user_data['grupo'])
        user.groups.add(grupo)

        # 🔹 Perfil (com verificação)
        PerfilUsuario.objects.get_or_create(user=user)
    
    print("Dados padrões verificados/criados com sucesso!")