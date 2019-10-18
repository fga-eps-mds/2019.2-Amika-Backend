from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Turma
from .serializers import TurmaSerializer, TurmaPeriodoSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
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
@permission_classes([IsAdminUser])
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
