# qualidade/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
from django.conf import settings

from .models import PerfilUsuario

GRUPOS_PADRAO = [
    'Qualidade',
    'Corte',
    'Injetora',
]

USUARIOS_PADRAO = [
    {
        'username': 'Qualidade01',
        'password': 'lynd1234',
        'grupo': 'Qualidade',
    },
    {
        'username': 'Operador01',
        'password': 'lynd1234',
        'grupo': 'Corte',
    },
    {
        'username': 'Injetora01',
        'password': 'lynd1234',
        'grupo': 'Injetora',
    },
]


@receiver(post_migrate)
def criar_dados_iniciais(sender, **kwargs):
    # 🔹 Criar grupos
    for nome_grupo in GRUPOS_PADRAO:
        Group.objects.get_or_create(name=nome_grupo)

    # 🔹 Criar usuários e perfis
    for user_data in USUARIOS_PADRAO:
        user, _ = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'password': make_password(user_data['password']),
                'is_active': True
            }
        )

        # 🔹 Grupo
        grupo = Group.objects.get(name=user_data['grupo'])
        user.groups.add(grupo)

        # 🔹 Perfil (somente se não existir)
        PerfilUsuario.objects.get_or_create(user=user)

