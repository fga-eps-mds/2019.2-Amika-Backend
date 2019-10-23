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

def autentica_administrador(view):
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        try:
            print(request.headers['Authorization'])
            token = {'token': request.headers['Authorization']}
            valid = VerifyJSONWebTokenSerializer().validate(token)
            user = User.objects.get(username=valid['user'])
            if user.is_superuser:
                return view(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Acesso permitido somente ao administrador'}, status=401)
        except:
            return JsonResponse({'error': 'Logue no sistema'}, status=401)
        print(valid)
    return wrapper

def autentica_aluno(view):
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        try:
            token = {'token': request.headers['Authorization']}
            valid = VerifyJSONWebTokenSerializer().validate(token)
            user = User.objects.get(username=valid['user'])
            return view(request, *args, **kwargs)
        except:
            return JsonResponse({'error': 'Logue no sistema'}, status=401)
    return wrapper

urlpatterns = [
    path('registro/', post, name='post_registro'),
    path('registros/',get, name='get_registros'),
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
]
