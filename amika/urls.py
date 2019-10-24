from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('registro/', post, name='post_registro'),
    path('registros/', get, name='get_registros'),
    path('registro/<int:pk>/', rud, name='rud_registro'),

    path('aluno/', post, name='post_aluno'),
    path('alunos/', get, name='get_alunos'),
    path('aluno/<int:pk>/', rud, name='rud_aluno'),

    path('turma/', post, name='post_turma'),
    path('turmas/', get, name='get_turmas'),
    path('turma/<int:pk>', rud, name='rud_turma'),

    path('grupo/', post, name='post_grupo'),
    path('grupos/', get, name='get_grupos'),
    path('grupo/<int:pk>/', rud, name='rud_grupo'),
    path('popula-grupo/', popula_grupos, name='popula_grupos'),

    path('agenda/', post, name="post_agendas"),
    path('agendas/', get, name="get_agendas"),
    path('agenda/<int:pk>', rud, name="rud_agenda"),

    path('enviar_anexo/', GerenciarAnexosView.as_view(), name='enviar_anexo'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)