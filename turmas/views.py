from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Turma
from .serializers import TurmaSerializer
from django.http import JsonResponse


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

def get_turma(pk):
	return Turma.objects.get(pk = pk)

@api_view(['DELETE'])
def deletar_turma(request,pk):
	Turma = get_turma(pk)
	Turma.delete()
	return JsonResponse({'turma deletada'})
	#return Response({"Turma deletada yay :3"})

@api_view(['PUT'])
def editar_turma(request, pk): 
	Turma = get_turma(pk)
	serializer_class = TurmaSerializer(Turma, partial = True, data = request.data)
	if serializer_class.is_valid(raise_exception = True):
		serializer_class.save()
		return Response(serializer_class.data)
	return Response ({"Turma editada"})