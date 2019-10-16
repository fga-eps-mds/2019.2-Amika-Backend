from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Turma, Agenda, Atividade
from .serializers import TurmaSerializer, TurmaPeriodoSerializer, AgendaSerializer
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404

@api_view(['GET', 'POST'])
def gerencia_turmas(request):
	return gerencia_objetos(request, Turma, TurmaPeriodoSerializer)

@api_view(['GET', 'DELETE' , 'PUT'])
def gerencia_turma(request, pk):
	return gerencia_objeto_pk(request, pk, Turma, TurmaSerializer)

@api_view(['POST', 'GET'])
def gerencia_agendas(request):
	return gerencia_objetos(request, Agenda, AgendaSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def gerencia_agenda(request, pk):
	return gerencia_objeto_pk(request, pk, Agenda, AgendaSerializer)

def gerencia_objetos(request, classe, serializer_class):
	if request.method == 'GET':
		queryset = classe.objects.all()	
		serializer = serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	if request.method == 'POST':
		serializer = serializer_class(data = request.data)
		if serializer.is_valid(raise_exception = True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def gerencia_objeto_pk(request, pk, classe, serializer_class):
	objeto = get_object_or_404(classe, pk=pk)

	if request.method == 'PUT':
		serializer = serializer_class(objeto, partial = True, data = request.data)
		if serializer.is_valid(raise_exception = True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		objeto.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	if request.method == 'GET':
		serializer = serializer_class(objeto)
		return Response(serializer.data, status=status.HTTP_200_OK)
