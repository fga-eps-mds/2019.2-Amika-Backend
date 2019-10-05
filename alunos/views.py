import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Registro, Aluno
from .serializers import AlunoSerializer, RegistroSerializer

URL_CHOICES = {
    'alunos': {
        'model': Aluno,
        'serializer': AlunoSerializer
    },
    'registros': {
        'model': Registro,
        'serializer': RegistroSerializer
    }
}


@api_view(['POST'])
def cadastra_aluno(request):
    if Registro.objects.filter(matricula=int(request.data['username']),
                               periodo__ano=datetime.date.today().year,
                               periodo__semestre=1 if datetime.date.today().month <= 6 else 2):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Aluno não matriculado no período atual."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def cadastra_registro(request):
    datas = []
    errors = []
    if request.data:
        for registro in request.data:
            serializer = RegistroSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                datas.append(serializer.data)
            else:
                errors.append([serializer.data, serializer.errors])
        if not errors:
            return Response(datas, status=status.HTTP_201_CREATED)
        else:
            return Response([datas, errors], status=status.HTTP_400_BAD_REQUEST)
    else:






@api_view(['GET'])
def lista_objetos(request, tipo):
    if tipo in URL_CHOICES:
        objs = URL_CHOICES[tipo]['model'].objects.all()
        serializer = URL_CHOICES[tipo]['serializer'](objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_registro(request, matricula):
    registro = Registro.objects.filter(matricula=matricula).first()
    if registro:
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
