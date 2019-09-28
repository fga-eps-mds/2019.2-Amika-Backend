from django.test import TestCase
from cadastrar_usuario.models import Aluno, Registrar
from cadastrar_usuario.serializers import AlunoSerializer, RegistrarSerializer, EditarAlunoSerializer

class SerializerAlunoCasoDeTeste(TestCase):
    def test_serializer_Aluno_valido(self):
        aluno = Aluno.objects.create(nome = 'Shiryu Amigo', matricula='170015311', senha = '918273645', email = 'shiryuamigo@unb.br')
        data = {'nome': aluno.nome, 'matricula': aluno.matricula, 'email': aluno.email, 'senha': aluno.senha}
        serializer = AlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        

    def test_serializer_Aluno_invalido(self):
        aluno = Aluno.objects.create(matricula='170015311', nome = '', senha = '918273645', email = 'shiryuamigo@unb.br')
        data = {'nome': aluno.nome, 'matricula': aluno.matricula, 'email': aluno.email, 'senha': aluno.senha}
        serializer = AlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class SerializerRegistrarSerializerCasoDeTeste(TestCase):
    def test_serializer_RegistrarSerializer_valido(self):
        aluno = Registrar.objects.create(matricula='170015311', turma='A')
        data = {'matricula': aluno.matricula, 'turma': aluno.turma}
        serializer = RegistrarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_Aluno_invalido(self):
        aluno = Registrar.objects.create(matricula='170015311', turma='')
        data = {'matricula': aluno.matricula, 'turma': aluno.turma}
        serializer = RegistrarSerializer(data=data)
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