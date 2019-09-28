from django.test import TestCase
from cadastrar_usuario.models import Aluno, Registro


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

class RegistroCasoDeTeste(TestCase):
    def criar_Registro(self, matricula="190015311", turma ="A"):
        return Registro.objects.create(matricula=matricula, turma=turma)

    def test_Registro_criacao(self):
        aluno = self.criar_Registro()
        self.assertTrue(isinstance(aluno, Registro))
        self.assertEqual(aluno.matricula, aluno.matricula)
        self.assertEqual(aluno.turma, aluno.turma)