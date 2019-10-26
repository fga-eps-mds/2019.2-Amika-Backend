import random

from django.apps import apps
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *

SERIALIZERS = {
    'Turma': TurmaSerializer,
    'Registro': RegistroSerializer,
    'Aluno': AlunoSerializer,
    'Grupo': GrupoSerializer,
    'Agenda': AgendaSerializer,
}


def serializer_status(serializer, success_status):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=success_status)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    if not request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    param = request.path.split('/')[1].title()
    if param == 'Aluno' and not Registro.objects.filter(matricula=request.data['username'],
                                                        periodo__ano=ano(),
                                                        periodo__semestre=semestre()):
        return Response({"Matrícula não registrada."}, status=status.HTTP_400_BAD_REQUEST)

    if param == 'Registro':
        serializer = SERIALIZERS[param](data=request.data, many=True)
    else:
        serializer = SERIALIZERS[param](data=request.data)

    return serializer_status(serializer, status.HTTP_201_CREATED)


@api_view(['GET'])
def get(request):
    param = request.path.split('/')[1].title()[:-1]
    model = apps.get_model("amika", param)
    objetos = model.objects.all()
    serializer = SERIALIZERS[param](objetos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def perfil_usuario(request, pk):
    param = request.path.split('/')[1].title()
    model = apps.get_model("amika", param)
    objeto = model.objects.filter(pk=pk).first()
    if not objeto:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.usuario.is_superuser or request.usuario.username == objeto.username:
        response = read(param, objeto)
        return response
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'PUT', 'DELETE'])
def rud(request, pk):
    param = request.path.split('/')[1].title()
    model = apps.get_model("amika", param)
    objeto = model.objects.filter(pk=pk).first()
    if not objeto:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = read(param, objeto)
    elif request.method == 'PUT':
        response = put(param, objeto, request.data)
    elif request.method == 'DELETE':
        response = delete(objeto)

    return response


def read(param, objeto):
    serializer = SERIALIZERS[param](objeto)
    return Response(serializer.data, status=status.HTTP_200_OK)


def put(param, objeto, data):
    serializer = SERIALIZERS[param](objeto, partial=True, data=data)
    return serializer_status(serializer, status.HTTP_200_OK)


def delete(objeto):
    objeto.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def popula_grupos(request):
    alunos = Aluno.objects.all()
    lista_alunos = [alunos[i] for i in random.sample(range(alunos.count()), alunos.count())]
    QNTD_ALUNOS_GRUPO = 15
    numero_alunos = 0
    numero_grupo = 1
    for aluno in lista_alunos:
        if numero_alunos == QNTD_ALUNOS_GRUPO:
            numero_alunos = 0
            numero_grupo += 1
        grupo, _ = Grupo.objects.get_or_create(nome='Grupo {}'.format(numero_grupo))
        aluno.grupo = grupo
        aluno.save()
        numero_alunos += 1

    if numero_alunos < QNTD_ALUNOS_GRUPO:
        grupo = Grupo.objects.get(nome='Grupo {}'.format(numero_grupo))
        alunos = grupo.aluno_set.all()
        for aluno in alunos:
            aluno.grupo = Grupo.objects.get(nome='Grupo {}'.format(list(alunos).index(aluno) + 1))
            aluno.save()

    return Response(status=status.HTTP_200_OK)
