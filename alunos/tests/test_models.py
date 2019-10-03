from django.test import TestCase

from alunos.models import Registro, Periodo, Aluno


class TestesPeriodo(TestCase):
    def setUp(self):
        Periodo.objects.create(ano=2019, semestre=2)

    def testa_str_do_objeto(self):
        self.assertEqual(str(Periodo.objects.first()), "2019/2")


class TestesRegistro(TestCase):
    def setUp(self):
        Registro.objects.create(
            matricula=123456789,
            turma="A",
            periodo=Periodo.objects.create(
                ano=2019,
                semestre=2))

    def testa_str_do_objeto(self):
        self.assertEqual(str(Registro.objects.first()), "A 123456789 2019/2")


class TestesAluno(TestCase):
    def setUp(self):
        Aluno.objects.create(
            username="123456789",
            first_name="Nome",
            last_name="Sobrenome",
            password="123",
            registro=Registro.objects.create(
                matricula=123456789,
                turma="A",
                periodo=Periodo.objects.create(
                    ano=2019,
                    semestre=2)))

    def testa_str_do_objeto(self):
        self.assertEqual(str(Aluno.objects.first()), "123456789 Nome Sobrenome")
