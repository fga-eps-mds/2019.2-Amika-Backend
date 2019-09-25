from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Turma
from .serializers import TurmaSerializer

@api_view(['POST'])
def listar_turmas(request):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    return Response({"Turma Cadastrada!"})



