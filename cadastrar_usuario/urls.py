from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_de_cadastro, name = 'tela_de_cadastro')
]