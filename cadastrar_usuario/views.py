from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UsuarioAluno
from .serializers import UsuarioAlunoSerializer

@api_view(['POST'])
def cadastrar_aluno(request):
	serializer = UsuarioAlunoSerializer(data = request.data)
	if serializer.isvalid():
		pessoa = UsuarioAlunoSerializer.create(serializer, request.data)
		return Response({"Aluno cadastrado com sucesso!"})
	else:
		return Response({"Dados incorretos! Tente novamente"})




