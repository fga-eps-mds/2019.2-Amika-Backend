from django.test import TestCase

from alunos.models import Aluno, Registro, Periodo
from alunos.serializers import AlunoSerializer, RegistroSerializer


class TestesAlunoSerializer(TestCase):
    def setUp(self):
        Registro.objects.create(
            matricula=123456789,
            turma="A",
            periodo=Periodo.objects.create(
                ano=2019,
                semestre=2))

    def testa_criacao_de_ojeto(self):
        aluno_dados = {
            'username': '123456789',
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'password': "123"
        }

        aluno = AlunoSerializer().create(aluno_dados)
        self.assertTrue(isinstance(aluno, Aluno))


class TestesRegistroSerializer(TestCase):
    def setUp(self):
        Periodo.objects.create(
            ano=2019,
            semestre=2)

    def testa_criacao_de_ojeto(self):
        registro_dados = {
            'matricula': 123456789,
            'turma': 'A'
        }

        registro = RegistroSerializer().create(registro_dados)
        self.assertTrue(isinstance(registro, Registro))
