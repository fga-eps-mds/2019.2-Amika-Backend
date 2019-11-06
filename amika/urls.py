from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    # Sem autenticação
    path('aluno/', post, name='post_aluno'),

    # Somente Administrador
    path('registro/', post, name='post_registro'),
    path('registros/', get, name='get_registros'),
    path('registro/<int:pk>/', rud, name='rud_registro'),

    path('alunos/', get, name='get_alunos'),

    path('turma/', post, name='post_turma'),
    path('turmas/', get, name='get_turmas'),
    path('turma/<int:pk>', rud, name='rud_turma'),

    path('grupo/', post, name='post_grupo'),
    path('grupos/', get, name='get_grupos'),
    path('popula-grupo/', popula_grupos, name='popula_grupos'),

    path('agenda/', post, name="post_agendas"),

    path('enviar_anexo/', GerenciarAnexosView.as_view(), name='enviar_anexo'),
    path('obter_nao_respondidas/', get_nao_respondidas, name='obter_nao_respondidas'),
    path('obter_respondidas/', get_respondidas, name="obter_respondidas"),
    path('obter_agenda/<int:pk>', get_agenda, name="obter_agenda"),
    path('editar_agenda/<int:pk>', GerenciarAnexosView.as_view(), name="editar_agenda"),

    path('material/', post, name="post_material"),

    # Autenticado
    path('aluno/<int:pk>/', rud, name='rud_aluno'),

    path('grupo/<int:pk>/', rud, name='rud_grupo'),

    path('agendas/', get, name="get_agendas"),
    path('agenda/<int:pk>', rud, name="rud_agenda"),

    path('materiais/', get, name="get_materiais"),
    path('material/<int:pk>', rud, name="rud_material"),

    # Aluno
    path('humor/', post, name="post_humor"),
    path('humors/', get, name="get_humors"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)