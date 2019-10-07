from django.test import TestCase
from turmas.models import Turma, Periodo
from turmas.serializers import TurmaSerializer

class TestesTurmaSerializer(TestCase):
    def setUp(self):
        Periodo.objects.create(
            ano=2019,
            semestre=2)

    def testa_criacao_de_objeto(self):
        turma_dados = {
            'nome':'Felicidade'
        }

        turma = TurmaSerializer().create(turma_dados)
        self.assertTrue(isinstance(turma, Turma))