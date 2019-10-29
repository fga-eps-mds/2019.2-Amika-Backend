from django.urls import path
from .views import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import redirect
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.response import Response
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.decorators import autentica_administrador, autentica_aluno

urlpatterns = [
    path('registro/', autentica_administrador(post), name='post_registro'),
    path('registros/', autentica_administrador(get), name='get_registros'),
    path('registro/<int:pk>/', autentica_administrador(rud), name='rud_registro'),

    path('aluno/', post, name='post_aluno'),
    path('alunos/', autentica_administrador(get), name='get_alunos'),
    path('aluno/<int:pk>/', autentica_administrador(rud), name='rud_aluno'),
    path('aluno/perfil/<int:pk>/', autentica_aluno(perfil_usuario), name='perfil_usuario'),

    path('turma/', autentica_administrador(post), name='post_turma'),
    path('turmas/', autentica_administrador(get), name='get_turmas'),
    path('turma/<int:pk>', autentica_administrador(rud), name='rud_turma'),

    path('grupo/', autentica_administrador(post), name='post_grupo'),
    path('grupos/', autentica_administrador(get), name='get_grupos'),
    path('grupo/<int:pk>/', autentica_administrador(rud), name='rud_grupo'),
    path('popula-grupo/', autentica_administrador(popula_grupos), name='popula_grupos'),

    path('agenda/', autentica_administrador(post), name="post_agendas"),
    path('agendas/', autentica_administrador(get), name="get_agendas"),
    path('agenda/<int:pk>', autentica_administrador(rud), name="rud_agenda"),

    path('material/', autentica_administrador(post), name="post_material"),
    path('materiais/', autentica_administrador(get), name="get_materiais"),
    path('material/<int:pk>', autentica_administrador(rud), name="rud_material"),

    path('humor/', post, name="post_humor"),
    path('humors/', get, name="get_humors"),
]
