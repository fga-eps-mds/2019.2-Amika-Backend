from rest_framework.test import APITestCase

from cadastrar_usuario.models import UsuarioAluno
from cadastrar_usuario.serializers import UsuarioAlunoSerializer


class AlunoTestCase(APITestCase):
    def setUp(self):
        self.aluno_atributos = {
            'nome_aluno': 'Aluno Teste',
            'matricula_aluno': '191234567',
            'email_aluno': 'alunoteste@email.com',
            'senha_aluno': 'alunoteste123'
        }

        self.dados_serializer = {
            'nome_aluno': 'Aluno Serializer',
            'matricula_aluno': '151234567',
            'email_aluno': 'alunoserializer@email.com',
            'senha_aluno': 'alunoserializer123'
        }

        self.aluno = UsuarioAluno.objects.create(**self.aluno_atributos)
        self.serializer = UsuarioAlunoSerializer(instance=self.dados_serializer)
