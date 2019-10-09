from django.contrib import admin
from django.urls import path, include
from .views import criar_grupo, gerencia_grupo, lista_grupos

urlpatterns = [
    path('gerencia_grupo/<int:pk>/', gerencia_grupo, name = 'gerencia_grupo'),
    path('lista_grupos/', lista_grupos, name = 'lista_grupos'),
    path('criar_grupo/', criar_grupo, name = 'criar_grupo'),
]
