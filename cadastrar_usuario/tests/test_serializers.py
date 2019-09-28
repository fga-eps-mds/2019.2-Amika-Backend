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

class SerializerRegistroSerializerCasoDeTeste(TestCase):
    def test_serializer_RegistroSerializer_valido(self):
        aluno = Registro.objects.create(matricula='170015311', turma='A')
        data = {'matricula': aluno.matricula, 'turma': aluno.turma}
        serializer = RegistroSerializer(data=data)
        self.assertFalse(serializer.is_valid())
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