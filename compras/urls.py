from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    # Requisições
    path('', views.home, name='home'),
    path('nova/', views.nova_requisicao, name='nova_requisicao'),
    path('editar/<int:requisicao_id>/', views.editar_requisicao, name='editar_requisicao'),
    
    # Cadastros
    path('cadastros/', views.cadastros, name='cadastros'),
    path('cadastros/modelo/novo/', views.cadastrar_modelo, name='cadastrar_modelo'),
    path('cadastros/modelo/editar/<int:modelo_id>/', views.editar_modelo, name='editar_modelo'),
    path('cadastros/cor/nova/', views.cadastrar_cor, name='cadastrar_cor'),
    path('cadastros/cor/editar/<int:cor_id>/', views.editar_cor, name='editar_cor'),
]