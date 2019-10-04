from django.urls import path, include
from turmas import views

urlpatterns = [
    path('turmas/', views.gerenciar_turmas, name = 'lista_turmas'),
    path('turma/<int:pk>', views.gerencia_turma, name = 'mostra_turma'),
]

