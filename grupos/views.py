from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Grupo
from .serializers import GrupoSerializer

@api_view(['POST'])
def criar_grupo(request):
    serializer = GrupoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def lista_grupos(request):
    print("ENTROU AQUI")
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




