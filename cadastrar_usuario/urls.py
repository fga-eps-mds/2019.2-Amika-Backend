from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_aluno, name = 'cadastrar_aluno')
]