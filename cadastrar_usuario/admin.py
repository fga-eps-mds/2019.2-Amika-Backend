from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .serializers import UsuarioAlunoSerializer, RegistrationSerializer, EditarAlunoSerializer
from .models import UsuarioAluno

class UsuarioProfessorAdmin(admin.ModelAdmin):
    add_serializer = UsuarioAlunoSerializer
    serializer = EditarAlunoSerializer
    model = UsuarioAluno
    list_display = ['matricula_aluno', 'nome_aluno', 'senha_aluno', 'email_aluno']

admin.site.register(UsuarioAluno, UsuarioProfessorAdmin)