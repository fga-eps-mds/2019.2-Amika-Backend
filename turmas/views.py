from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Turma
from .serializers import TurmaSerializer

@api_view(['GET'])
def listar_turmas(request):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer(queryset, many=True)
    return Response(serializer_class.data)

@api_view(['POST'])
def criar_turmas(request):
	serializer = TurmaSerializer(data = request.data)
	if serializer.is_valid():
		turma = TurmaSerializer.create(serializer, request.data)
		return Response ({'Turma Criada!'})
	else:
		return Response ({'Deu errado bro'})