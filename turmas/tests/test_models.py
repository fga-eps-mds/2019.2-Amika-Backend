from django.test import TestCase
from turmas.models import Turma, Periodo

class TestesPeriodo(TestCase):
    def setUp(self):
        Periodo.objects.create(ano=2019, semestre=2)

    def testa_str_do_objeto(self):
        self.assertEqual(str(Periodo.objects.first()), "2019/2")

class TestesTurma(TestCase):
    def setUp(self):
        Turma.objects.create(
            nome = "Felicidade",
            periodo = Periodo.objects.create(ano=2019, semestre=2)
        )

    def testa_str_do_objeto(self):
        self.assertEqual(str(Turma.objects.first()), "Felicidade 2019/2")
