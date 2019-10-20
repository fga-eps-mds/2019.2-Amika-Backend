from django.test import TestCase

from amika.models import *


class TestesPeriodo(TestCase):
    def testa_str_do_objeto(self):
        periodo = Periodo.objects.create(ano=2019, semestre=2)
        self.assertEqual(str(periodo), "2019/2")


class TestesTurma(TestCase):
    def testa_str_do_objeto(self):
        turma = Turma.objects.create(descricao="A")
        self.assertEqual(str(turma), "A")


class TestesRegistro(TestCase):
    def testa_str_do_objeto(self):
        registro = Registro.objects.create(
            matricula=123456789,
            turma=Turma.objects.create(descricao="A"),
            periodo=Periodo.objects.create(ano=2019, semestre=2))
        self.assertEqual(str(registro), "2019/2 A 123456789")


class TestesAluno(TestCase):
    def testa_str_do_objeto(self):
        aluno = Aluno.objects.create(
            username="123456789",
            first_name="Nome",
            last_name="Sobrenome",
            password="123",
            registro=Registro.objects.create(
                matricula=123456789,
                turma=Turma.objects.create(descricao="A"),
                periodo=Periodo.objects.create(ano=2019, semestre=2)))
        self.assertEqual(str(aluno), "123456789 Nome Sobrenome")


class TestesGrupo(TestCase):
    def testa_str_do_objeto(self):
        grupo = Grupo.objects.create(nome="Grupo 1")
        self.assertEqual(str(grupo), "Grupo 1")


class TestesAgenda(TestCase):
    def testa_str_do_objeto(self):
        agenda = Agenda.objects.create(
            nome="Atividade 2",
            descricao="descricao agenda...",
            tipo="Individual",
            data_disponibilizacao="2019-09-09",
            data_encerramento="2019-09-10")
        self.assertEqual(str(agenda), "Atividade 2 Individual 2019-09-09/2019-09-10")


class TestesFormulario(TestCase):
    def testa_str_do_objeto(self):
        formulario = Formulario.objects.create(tipo="A", pontuacao="10.00")
        self.assertEqual(str(formulario), "A 10.00")
