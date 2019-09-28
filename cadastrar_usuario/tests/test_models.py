from django.test import TestCase
from cadastrar_usuario.models import Aluno, Registrar


class AlunoCasoDeTeste(TestCase):
    def criar_Aluno(self, matricula="190015311", nome="Carlos Marcio", senha="192837465", email="carlosmarcio@unb.br"):
        return Aluno.objects.create(matricula=matricula, nome=nome, senha=senha, email=email)

    def test_Aluno_criacao(self):
        aluno = self.criar_Aluno()
        self.assertTrue(isinstance(aluno, Aluno))
        self.assertEqual(aluno.matricula, aluno.matricula)
        self.assertEqual(aluno.nome, aluno.nome)
        self.assertEqual(aluno.senha, aluno.senha)
        self.assertEqual(aluno.email, aluno.email)

class RegistrarCasoDeTeste(TestCase):
    def criar_Registrar(self, matricula="190015311", turma ="A"):
        return Registrar.objects.create(matricula=matricula, turma=turma)

    def test_Registrar_criacao(self):
        aluno = self.criar_Registrar()
        self.assertTrue(isinstance(aluno, Registrar))
        self.assertEqual(aluno.matricula, aluno.matricula)
        self.assertEqual(aluno.turma, aluno.turma)