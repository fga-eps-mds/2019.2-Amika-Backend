from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .serializers import UsuarioAlunoSerializer, RegistrationSerializer, EditarAlunoSerializer
from .models import UsuarioAluno

class UsuarioAlunoAdmin(admin.ModelAdmin):
    add_form = UsuarioAlunoSerializer
    form = EditarAlunoSerializer
    model = UsuarioAluno
    list_display = ["__all__"]

admin.site.register(UsuarioAluno, UsuarioAlunoAdmin)