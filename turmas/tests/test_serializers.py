from django.test import TestCase
from turmas.models import Turma
from turmas.serializers import TurmaSerializer

class TurmaSerializerCasosDeTestes(TestCase):
    def testa_serializer_valido_turma(self):
        turma = Turma.objects.create(
            nome_turma = "Felicidade",
            ano_turma = 2019,
            periodo_turma = 2
        )

        turma_dados = {
            'nome_turma': turma.nome_turma,
            'ano_turma': turma.ano_turma,
            'periodo_turma': turma.periodo_turma
        }

        serializer_turma = TurmaSerializer(data=turma_dados)
        self.assertTrue(serializer_turma.is_valid())

    def testa_serializer_invalido_turma(self):
        turma = Turma.objects.create(
            nome_turma = "",
            ano_turma = 2019,
            periodo_turma = 2
        )

        turma_dados = {
            'nome_turma': turma.nome_turma,
            'ano_turma': turma.ano_turma,
            'periodo_turma': turma.periodo_turma
        }

        serializer_turma = TurmaSerializer(data=turma_dados)
        self.assertFalse(serializer_turma.is_valid())
        