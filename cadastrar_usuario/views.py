from django.shortcuts import render
from cadastrar_usuario.models import User
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer

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

@api_view(['POST'])
def set_registration_list(request):
    serializer = RegistrationSerializer(data = request.data)
    if serializer.is_valid():
        matricula = RegistrationSerializer.create(serializer, request.data)
        return Response({"Matricula": request.data['matricula'], "turma": request.data['turma']})
    else:
        return Response({"message": "Entre com os atributos corretos!", "atributos_esperados": "matricula, turma"})