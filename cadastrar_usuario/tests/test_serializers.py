from django.test import TestCase
from cadastrar_usuario.models import UsuarioAluno, Registrar
from cadastrar_usuario.serializers import UsuarioAlunoSerializer, RegistrarSerializer, EditarAlunoSerializer

class SerializerUsuarioAlunoCasoDeTeste(TestCase):
    def test_serializer_UsuarioAluno_valido(self):
        Aluno = UsuarioAluno.objects.create(nome_aluno = 'Shiryu Amigo', matricula_aluno='170015311', senha_aluno = '918273645', email_aluno = 'shiryuamigo@unb.br')
        data = {'nome_aluno': Aluno.nome_aluno, 'matricula_aluno': Aluno.matricula_aluno, 'email_aluno': Aluno.email_aluno, 'senha_aluno': Aluno.senha_aluno}
        serializer = UsuarioAlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        

    def test_serializer_UsuarioAluno_invalido(self):
        Aluno = UsuarioAluno.objects.create(matricula_aluno='170015311', nome_aluno = '', senha_aluno = '918273645', email_aluno = 'shiryuamigo@unb.br')
        data = {'nome_aluno': Aluno.nome_aluno, 'matricula_aluno': Aluno.matricula_aluno, 'email_aluno': Aluno.email_aluno, 'senha_aluno': Aluno.senha_aluno}
        serializer = UsuarioAlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class SerializerRegistrarSerializerCasoDeTeste(TestCase):
    def test_serializer_RegistrarSerializer_valido(self):
        Aluno = Registrar.objects.create(matricula='170015311', turma='A')
        data = {'matricula': Aluno.matricula, 'turma': Aluno.turma}
        serializer = RegistrarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_UsuarioAluno_invalido(self):
        Aluno = Registrar.objects.create(matricula='170015311', turma='')
        data = {'matricula': Aluno.matricula, 'turma': Aluno.turma}
        serializer = RegistrarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class SerializerEditarAlunoCasoDeTeste(TestCase):
    def test_serializer_EditarAluno_valido(self):
        Aluno = UsuarioAluno.objects.create(nome_aluno = 'Shiryu Amigo', matricula_aluno='170015311', senha_aluno = '918273645', email_aluno = 'shiryuamigo@unb.br')
        data = {'nome_aluno': Aluno.nome_aluno, 'matricula_aluno': Aluno.matricula_aluno, 'email_aluno': Aluno.email_aluno, 'senha_aluno': Aluno.senha_aluno}
        serializer = EditarAlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_EditarAluno_invalido(self):
        Aluno = UsuarioAluno.objects.create(matricula_aluno='170015311', nome_aluno = '', senha_aluno = '918273645', email_aluno = 'shiryuamigo@unb.br')
        data = {'nome_aluno': Aluno.nome_aluno, 'matricula_aluno': Aluno.matricula_aluno, 'email_aluno': Aluno.email_aluno, 'senha_aluno': Aluno.senha_aluno}
        serializer = EditarAlunoSerializer(data=data)
        self.assertFalse(serializer.is_valid())