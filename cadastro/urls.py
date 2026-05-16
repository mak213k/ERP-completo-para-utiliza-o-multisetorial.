# polls/urls.py — CRIE este arquivo
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_cliente, name='cadastro'),
    path('entrega/', views.gerar_entrega, name='gerar_entrega'),
    path('relatorio/', views.lista_entregas, name='lista_entregas'),
]