from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import formulario_felicidade
from .serializers import FormuarioFelicidadeSerializer

@api_view(['POST'])
def gerencia_formulario_felicidade(request):

	if request.method == 'POST':
		serializer = FormuarioFelicidadeSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
