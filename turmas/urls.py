from django.urls import path, include
from turmas import views

urlpatterns = [
    path('', views.listar_turmas, name = 'lista_turmas'),
    path('cadastro', views.criar_turmas, name = 'cria_turmas'),
    path('turma/<int:pk>', views.get_turma, name = 'mostra_turma'),
]

