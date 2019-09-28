from django.test import TestCase

from cadastrar_usuario.models import Aluno, Registro
from cadastrar_usuario.serializers import AlunoSerializer, RegistroSerializer, EditarAlunoSerializer


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
    def test_serializer_EditarAluno_valido(self):
        aluno = Aluno.objects.create(nome = 'Shiryu Amigo', matricula='170015311', senha = '918273645', email = 'shiryuamigo@unb.br')
        data = {'nome': aluno.nome, 'matricula': aluno.matricula, 'email': aluno.email, 'senha': aluno.senha}
        serializer = EditarAlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_EditarAluno_invalido(self):
        aluno = Aluno.objects.create(matricula='170015311', nome = '', senha = '918273645', email = 'shiryuamigo@unb.br')
        data = {'nome': aluno.nome, 'matricula': aluno.matricula, 'email': aluno.email, 'senha': aluno.senha}
        serializer = EditarAlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())