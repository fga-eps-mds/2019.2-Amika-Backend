from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Turma
from .serializers import TurmaSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def gerenciar_turmas(request):
	if request.method == 'GET':
		queryset = Turma.objects.all()
		serializer_class = TurmaSerializer(queryset, many=True)
		return Response(serializer_class.data, status=status.HTTP_200_OK)

	if request.method == 'POST':
		serializer = TurmaSerializer(data = request.data)
		if serializer.is_valid():
			turma = TurmaSerializer.create(serializer, request.data)
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response (serializer.erros, status=status.HTPP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE' , 'PUT'])
def gerencia_turma(request, pk):
	turma = Turma.objects.filter(pk = pk).first()

	if request.method == 'GET':
		queryset = Turma.objects.get(pk = pk)
		serializer_class = TurmaSerializer(queryset)
		return Response (serializer_class.data, status=status.HTTP_200_OK)

	if request.method == 'DELETE':
		turma.delete()
		return Response({'turma deletada'}, status=status.HTTP_204_NO_CONTENT)

	if request.method == 'PUT':
		serializer_class = TurmaSerializer(turma, partial = True, data = request.data)
		if serializer_class.is_valid(raise_exception = True):
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_200_OK)
		return Response ({"Turma editada"})
