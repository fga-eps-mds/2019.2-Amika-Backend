from rest_framework.test import APITestCase
from cadastrar_usuario.serializers import AlunoSerializer
from django.test import TestCase

from cadastrar_usuario.models import Aluno, Registro
from cadastrar_usuario.serializers import AlunoSerializer, RegistroSerializer, EditarAlunoSerializer


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

        self.aluno = Aluno.objects.create(**self.aluno_atributos)
        self.serializer = AlunoSerializer(instance=self.dados_serializer)

class AlunoSerializerCasosDeTestes(TestCase):
    def testa_serializer_valido_aluno(self):
        aluno = Aluno.objects.create(
            nome='Shiryu Amigo',
            matricula='170015311',
            senha='918273645',
            email='shiryuamigo@unb.br')

        aluno_dados = {
            'nome': aluno.nome,
            'matricula': aluno.matricula,
            'email': aluno.email,
            'senha': aluno.senha
        }

        serializer_aluno = AlunoSerializer(data=aluno_dados)
        self.assertTrue(serializer_aluno.is_valid())

    def testa_serializer_invalido_aluno(self):
        aluno = Aluno.objects.create(
            nome='',
            matricula='170015311',
            senha='918273645',
            email='shiryuamigo@unb.br')

        aluno_dados = {
            'nome': aluno.nome,
            'matricula': aluno.matricula,
            'email': aluno.email,
            'senha': aluno.senha
        }

        serializer_aluno = AlunoSerializer(data=aluno_dados)
        self.assertFalse(serializer_aluno.is_valid())


class RegistroSerializerCasoDeTeste(TestCase):
    def testa_serializer_valido_registro_serializer(self):
        registro = Registro.objects.create(
            matricula='170015311',
            turma='A')

        registro_dados = {
            'matricula': registro.matricula,
            'turma': registro.turma
        }

        serializer_registro = RegistroSerializer(data=registro_dados)
        self.assertTrue(serializer_registro.is_valid())

    def testa_serializer_invalido_registro_serializer(self):
        registro = Registro.objects.create(
            matricula='170015311',
            turma='')

        registro_dados = {
            'matricula': registro.matricula,
            'turma': registro.turma
        }

        serializer = RegistroSerializer(data=registro_dados)
        self.assertFalse(serializer.is_valid())


class SerializerEditarAlunoCasoDeTeste(TestCase):
    def testa_serializer_valido_editar_aluno_serializer(self):
        aluno = Aluno.objects.create(
            nome='Shiryu Amigo',
            matricula='170015311',
            senha='918273645',
            email='shiryuamigo@unb.br')

        aluno_dados = {
            'nome': aluno.nome,
            'matricula': aluno.matricula,
            'email': aluno.email,
            'senha': aluno.senha
        }

        serializer = EditarAlunoSerializer(data=aluno_dados)
        self.assertTrue(serializer.is_valid())

    def testa_serializer_invalido_editar_aluno_serializer(self):
        aluno = Aluno.objects.create(
            matricula='170015311',
            nome='',
            senha='918273645',
            email='shiryuamigo@unb.br')

        aluno_dados = {
            'nome': aluno.nome,
            'matricula': aluno.matricula,
            'email': aluno.email,
            'senha': aluno.senha
        }

        serializer = EditarAlunoSerializer(data=aluno_dados)
        self.assertFalse(serializer.is_valid())
