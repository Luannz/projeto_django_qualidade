from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def somente_loja(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verifica se é superusuário (pode acessar tudo)
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        
        # Verifica se o usuário está no grupo "Loja"
        if request.user.groups.filter(name='Loja').exists():
            return view_func(request, *args, **kwargs)
        
        # Verifica se tem profile.tipo == 'Loja' (caso use Profile)
        if hasattr(request.user, 'profile') and request.user.profile.tipo == 'Loja':
            return view_func(request, *args, **kwargs)
        
        # Se não tiver permissão, redireciona
        messages.error(request, 'Acesso negado. Área restrita para usuários da loja.')
        return redirect('home')
    
    return wrapper