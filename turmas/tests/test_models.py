from django.test import TestCase
from turmas.models import Turma

class TurmaCasosDeTeste(TestCase):
    def criar_turma(self):
        turma = Turma.objects.create(
            nome_turma = "Felicidade",
            ano_turma = 2019,
            periodo_turma = 2
        )
        return turma
    
    def testa_criacao_turma(self):
        turma = self.criar_turma()
        self.assertTrue(isinstance(turma, Turma))
        self.assertEqual(turma.nome_turma, "Felicidade")
        self.assertEqual(turma.ano_turma, 2019)
        self.assertEqual(turma.periodo_turma, 2)
