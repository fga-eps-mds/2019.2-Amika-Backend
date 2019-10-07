from django.urls import path, include
from turmas import views

urlpatterns = [
    path('turmas/', views.gerencia_turmas, name = 'gerencia_turmas'),
    path('turma/<int:pk>', views.gerencia_turma, name = 'gerencia_turma'),
]

