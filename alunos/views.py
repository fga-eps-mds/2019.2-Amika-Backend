import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Registro, Aluno
from .serializers import AlunoSerializer, RegistroSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
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


@api_view(['GET'])
def lista_alunos(request):
    alunos = Aluno.objects.all()
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def cadastra_registro(request):
    serializer = RegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_registros(request):
    registros = Registro.objects.all()
    serializer = RegistroSerializer(registros, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove_registro(request, matricula):
    registro = Registro.objects.filter(matricula=str(matricula)).first()
    if registro:
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
