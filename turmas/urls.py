from django.urls import path, include
from turmas import views

urlpatterns = [
    path('turmas', views.listar_turmas),
    path('turmas_create', views.criar_turmas),
    path('turma_delete/<int:pk>', views.deletar_turma),
    path('turma_edit/<int:pk>', views.editar_turma),
]
