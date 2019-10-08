from django.urls import path

from alunos.views import cadastra_aluno, cadastra_registro, lista_objetos, remove_registro

urlpatterns = [
    path('aluno/', cadastra_aluno, name='cadastra_aluno'),
    path('registro/', cadastra_registro, name='cadastra_registro'),
    path('<str:tipo>/', lista_objetos, name='lista_objetos'),
    path('registro/<int:matricula>/', remove_registro, name='remove_registro'),
]
