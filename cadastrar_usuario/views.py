from django.shortcuts import render
from cadastrar_usuario.models import User
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from .models import Registration
from rest_framework import generics

#Criar o form SubForm
def tela_de_cadastro(request):
    """if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            return redirect('tela_de_cadastro')

    else:
        form = SubForm()
    return render(request, 'cadastrar_usuario/tela_de_cadastro.html', {'form': form})"""
    pass

@api_view(['GET', 'POST'])
def set_registration_list(self, request):
    data = request.data.get("items") if 'items' in request.data else request.data
    many = isinstance(data, list)
    print (data, many)
    serializer = self.get_serializer(data=data, many=many)
    #serializer = RegistrationSerializer(data = request.data)
    if request.method == 'POST':
        if serializer.is_valid():
            self.perform_create(serializer)
            #matricula = RegistrationSerializer.create(serializer, request.data)
            return Response({"Matricula": request.data['matricula'], "turma": request.data['turma']})
        else:
            return Response({"message": "Entre com os atributos corretos!", "atributos_esperados": "matricula, turma"})
    else:
        matriculas = Registration.objects.all()
        serializer = RegistrationSerializer(matriculas, many = True)
        return Response(serializer.data)

        #serializer.is_valid(raise_exception=True)
        #headers = self.get_success_headers(serializer.data)
        #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RegistrationViewSet(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get("items") if 'items' in request.data else request.data
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        return Response({"Matricula": request.data['matricula'], "turma": request.data['turma']})