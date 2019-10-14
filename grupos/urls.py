from django.urls import path

from .views import cria_grupo, gerencia_grupo, lista_grupos, popula_grupos

urlpatterns = [
    path('grupo/', cria_grupo, name='cria_grupo'),
    path('grupos/', lista_grupos, name='lista_grupos'),
    path('grupo/<int:pk>/', gerencia_grupo, name='gerencia_grupo'),
    path('popula-grupo/', popula_grupos, name='popula_grupos'),
]
