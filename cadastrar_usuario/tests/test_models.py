from django.test import TestCase
from cadastrar_usuario.models import UsuarioAluno, Registrar


class UsuarioAlunoCasoDeTeste(TestCase):
    def criar_UsuarioAluno(self, matricula_aluno="190015311", nome_aluno="Carlos Marcio", senha_aluno="192837465", email_aluno="carlosmarcio@unb.br"):
        return UsuarioAluno.objects.create(matricula_aluno=matricula_aluno, nome_aluno=nome_aluno, senha_aluno=senha_aluno, email_aluno=email_aluno)

    def test_UsuarioAluno_criacao(self):
        Aluno = self.criar_UsuarioAluno()
        self.assertTrue(isinstance(Aluno, UsuarioAluno))
        self.assertEqual(Aluno.matricula_aluno, Aluno.matricula_aluno)
        self.assertEqual(Aluno.nome_aluno, Aluno.nome_aluno)
        self.assertEqual(Aluno.senha_aluno, Aluno.senha_aluno)
        self.assertEqual(Aluno.email_aluno, Aluno.email_aluno)