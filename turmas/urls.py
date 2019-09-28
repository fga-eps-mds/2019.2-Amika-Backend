from django.urls import path, include
from turmas import views

urlpatterns = [
    path('turmas/', views.listar_turmas, name = 'lista_turmas'),
    path('turmas_create', views.criar_turmas, name = 'cria_turmas'),
    path('turma_delete/<int:pk>', views.deletar_turma, name = 'deleta_turma'),
    path('turma_edit/<int:pk>', views.editar_turma, name = 'edita_turma'),
    path('turma/<int:pk>', views.get_turma),
]

