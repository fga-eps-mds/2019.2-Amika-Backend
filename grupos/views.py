import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from alunos.models import Aluno
from .models import Grupo
from .serializers import GrupoSerializer


@api_view(['POST'])
def cria_grupo(request):
    if request.data:
        serializer = GrupoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_grupos(request):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer(queryset, many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
def gerencia_grupo(request, pk):
    grupo = Grupo.objects.filter(pk=pk).first()
    if not grupo:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return mostra_grupo(grupo)
    elif request.method == 'PUT':
        return edita_grupo(grupo, request.data)
    elif request.method == 'DELETE':
        return deleta_grupo(grupo)


def mostra_grupo(grupo):
    serializer_class = GrupoSerializer(grupo)
    return Response(serializer_class.data, status=status.HTTP_200_OK)


def edita_grupo(grupo, alteracoes):
    serializer = GrupoSerializer(grupo, partial=True, data=alteracoes)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def deleta_grupo(grupo):
    grupo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def popula_grupos():
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
            aluno.grupo = Grupo.objects.get(nome='Grupo {}'.format(alunos.index(aluno)))
            aluno.save()

    return Response(status=status.HTTP_200_OK)
