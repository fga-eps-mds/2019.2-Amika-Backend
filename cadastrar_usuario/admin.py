from django.contrib import admin

from .models import Aluno
from .serializers import AlunoSerializer, EditarAlunoSerializer


class Professor(admin.ModelAdmin):
    fields = (
        'matricula',
    )

    add_serializer = AlunoSerializer
    serializer = EditarAlunoSerializer
    model = Aluno

    list_display = (
        'matricula',
        'nome',
        'email',
    )


admin.site.register(Aluno, Professor)
