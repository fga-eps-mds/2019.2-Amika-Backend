from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Aluno, Registro
from .serializers import AlunoSerializer, RegistroSerializer

@api_view(['POST'])
def cadastrar_aluno(request):
	serializer = AlunoSerializer(data = request.data)
	if serializer.is_valid():
		registro = Registro.objects.filter(matricula=serializer.data["matricula"]).first()
		if (registro):
			aluno = AlunoSerializer.create(serializer, request.data)
			return Response ({"Usuario cadastrado com sucesso!"})
		else:
			return Response ({"Não foi possível encontrar um aluno com esta matricula na disciplina, tente novamente!"})		
	else:
		return Response({"Dados incorretos! Tente novamente"})

class RegistrosMultiplosViewSet(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get("items") if 'items' in request.data else request.data
        many_data = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({request})


