from django.urls import path

from alunos.views import cadastra_aluno, lista_alunos, cadastra_registro, lista_registros, remove_registro

urlpatterns = [
    path('aluno/', cadastra_aluno, name='cadastra_aluno'),
    path('alunos/', lista_alunos, name='lista_alunos'),
    path('registro/', cadastra_registro, name='cadastra_registro'),
    path('registros/', lista_registros, name='lista_registros'),
    path('registro/<int:matricula>/', remove_registro, name='remove_registro'),
]
