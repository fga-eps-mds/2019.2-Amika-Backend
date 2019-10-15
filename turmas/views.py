from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Turma, Agenda, Atividade
from .serializers import TurmaSerializer, TurmaPeriodoSerializer, AgendaSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def gerencia_turmas(request):
	if request.method == 'GET':
		queryset = Turma.objects.all()
		serializer_class = TurmaPeriodoSerializer(queryset, many=True)
		return Response(serializer_class.data, status=status.HTTP_200_OK)

	if request.method == 'POST':
		serializer = TurmaSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE' , 'PUT'])
def gerencia_turma(request, pk):
	turma = Turma.objects.filter(pk = pk).first()

	if not turma:
		return Response(status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		serializer_class = TurmaSerializer(turma)
		return Response(serializer_class.data, status=status.HTTP_200_OK)

	if request.method == 'DELETE':
		turma.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	if request.method == 'PUT':
		serializer_class = TurmaSerializer(turma, partial = True, data = request.data)
		if serializer_class.is_valid(raise_exception = True):
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_200_OK)
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def gerencia_agendas(request):
	request.POST._mutable = True 
	if request.method == 'GET':
		queryset = Agenda.objects.all()
		serializer = AgendaSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	if request.method == 'POST':
		serializer = AgendaSerializer(data = request.data)
		if serializer.is_valid():
			if request.data['data_disponibilizacao'] < request.data['data_encerramento']:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				 Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def gerencia_agenda(request, pk):
	agenda = Agenda.objects.filter(pk = pk).first()
	
	if request.method == 'PUT':
		serializer = AgendaSerializer(agenda, partial = True, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		agenda.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	if request.method == 'GET':
		serializer = AgendaSerializer(agenda)
		return Response(serializer.data, status=status.HTTP_200_OK)
		