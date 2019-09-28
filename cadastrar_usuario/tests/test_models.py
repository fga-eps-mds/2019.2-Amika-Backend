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
        self.assertEqual(aluno.matricula, "190015311")
        self.assertEqual(aluno.nome, "Carlos Marcio")
        self.assertEqual(aluno.senha, "192837465")
        self.assertEqual(aluno.email, "carlosmarcio@unb.br")


class RegistroCasosDeTestes(TestCase):
    def criar_registro(self):
        registro = Registro.objects.create(
            matricula="190015311",
            turma="A")

        return registro

    def testa_criacao_registro(self):
        registro = self.criar_registro()

        self.assertTrue(isinstance(registro, Registro))
        self.assertEqual(registro.matricula, "190015311")
        self.assertEqual(registro.turma, "A")
