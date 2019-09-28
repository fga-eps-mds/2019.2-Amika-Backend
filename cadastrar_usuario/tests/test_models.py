from django.test import TestCase

from cadastrar_usuario.models import Aluno, Registro


class AlunoCasosDeTestes(TestCase):
    def criar_aluno(self):
        aluno = Aluno.objects.create(
            matricula="190015311",
            nome="Carlos Marcio",
            senha="192837465",
            email="carlosmarcio@unb.br")

        return aluno

    def testa_criacao_aluno(self):
        aluno = self.criar_aluno()

        self.assertTrue(isinstance(aluno, Aluno))
class RegistroCasoDeTeste(TestCase):
    def criar_Registro(self, matricula="190015311", turma ="A"):
        return Registro.objects.create(matricula=matricula, turma=turma)

    def test_Registro_criacao(self):
        aluno = self.criar_Registro()
        self.assertTrue(isinstance(aluno, Registro))
        self.assertEqual(aluno.matricula, aluno.matricula)
        self.assertEqual(aluno.turma, aluno.turma)        self.assertEqual(aluno.matricula, "190015311")
        self.assertEqual(aluno.nome, "Carlos Marcio")
        self.assertEqual(aluno.senha, "192837465")
        self.assertEqual(aluno.email, "carlosmarcio@unb.br")


