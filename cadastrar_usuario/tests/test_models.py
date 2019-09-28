from django.test import TestCase
from cadastrar_usuario.models import UsuarioAluno, Registrar


class UsuarioAlunoCasoDeTeste(TestCase):
    def criar_UsuarioAluno(self, matricula_aluno="190015311", nome_aluno="Carlos Marcio", senha_aluno="192837465", email_aluno="carlosmarcio@unb.br"):
        return UsuarioAluno.objects.create(matricula_aluno=matricula_aluno, nome_aluno=nome_aluno, senha_aluno=senha_aluno, email_aluno=email_aluno)

    def test_UsuarioAluno_criacao(self):
        aluno = self.criar_UsuarioAluno()
        self.assertTrue(isinstance(aluno, UsuarioAluno))
        self.assertEqual(aluno.matricula_aluno, aluno.matricula_aluno)
        self.assertEqual(aluno.nome_aluno, aluno.nome_aluno)
        self.assertEqual(aluno.senha_aluno, aluno.senha_aluno)
        self.assertEqual(aluno.email_aluno, aluno.email_aluno)

class RegistrarCasoDeTeste(TestCase):
    def criar_Registrar(self, matricula="190015311", turma ="A"):
        return Registrar.objects.create(matricula=matricula, turma=turma)

    def test_Registrar_criacao(self):
        aluno = self.criar_Registrar()
        self.assertTrue(isinstance(aluno, Registrar))
        self.assertEqual(aluno.matricula, aluno.matricula)
        self.assertEqual(aluno.turma, aluno.turma)