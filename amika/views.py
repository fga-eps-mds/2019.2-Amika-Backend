import json
import random

from django.apps import apps
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime, date, timedelta

from .serializers import *

SERIALIZERS = {
    'Turma': TurmaSerializer,
    'Registro': RegistroSerializer,
    'Aluno': AlunoSerializer,
    'Grupo': GrupoSerializer,
    'Agenda': AgendaSerializer,
    'AgendaRealizada': AgendaRealizadaSerializer,
    'Humor': HumorSerializer,
    'Material': MaterialSerializer,
    'Formulario': FormularioSerializer,
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
    param = 'AgendaRealizada' if param == 'Agenda-Realizada' else param

    if param == 'Registro':
        serializer = SERIALIZERS[param](data=request.data, many=True)

    else:
        serializer = SERIALIZERS[param](data=request.data)

    return serializer_status(serializer, status.HTTP_201_CREATED)


@api_view(['GET'])
def get(request):
    param = request.path.split('/')[1].title()[:-1]
    if param in ['Materiai', 'Agendas-Realizada', 'Agendas-Nao-Realizada']:
        if param == 'Materiai':
            param = 'Material'
        else:
            param = 'AgendaRealizada'

    model = apps.get_model("amika", param)
    objetos = model.objects.all()
    serializer = SERIALIZERS[param](objetos, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_alunos_grupo(request):
    param = 'Aluno'
    grupo = Grupo.objects.filter(aluno = request.user.id).first()
    alunos = Aluno.objects.filter(grupo = grupo)
    serializer = SERIALIZERS[param](alunos, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK )


@api_view(['GET'])
def agendas_realizadas_aluno(request, pk):
    agendas_realizadas = []
    for r in AgendaRealizada.objects.select_related('agenda').filter(aluno_id=pk):
        agendas_realizadas.append({
            "agenda": AgendaSerializer(r.agenda).data,
            "realizacao": AgendaRealizadaSerializer(r).data
        })

    return Response(json.dumps(agendas_realizadas), status=status.HTTP_200_OK)


@api_view(['GET'])
def agendas_nao_realizadas_aluno(request, pk):
    agendas_nao_realizadas = Agenda.objects.exclude(
        id__in=AgendaRealizada.objects.filter(aluno_id=pk).values('agenda_id'))
    serializer = AgendaSerializer(agendas_nao_realizadas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def humor_turma(request, pk):
    turma = Turma.objects.filter(pk=pk)
    registro = Registro.objects.filter(turma = turma[0])
    aluno = Aluno.objects.filter(registro__in = registro)
    humores = Humor.objects.filter(aluno__in = aluno).order_by('data')
    # serializer = HumorSerializer(humores, many = True)
    data_inicial = humores.first().data
    data_final = humores.last().data
    soma = 0
    medias = []
    numero_humores = 0
    datas = []
    while data_final >= data_inicial:
        datas.append(data_inicial)
        humores_dia = humores.filter(data = data_inicial)
        for humor in humores_dia:
            soma += humor.humor_do_dia
            numero_humores += 1
        medias.append(float("{0:.1f}".format(soma/numero_humores)))
        soma = 0
        numero_humores = 0
        data_inicial += timedelta(days = 1)
        

    return Response({"medias": medias, "datas": datas})    


@api_view(['GET', 'PUT', 'DELETE'])
def rud(request, pk):
    param = request.path.split('/')[1].title()
    param = 'AgendaRealizada' if param == 'Agenda-Realizada' else param

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
