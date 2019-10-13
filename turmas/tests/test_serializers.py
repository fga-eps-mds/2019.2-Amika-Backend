from django.test import TestCase
from turmas.models import Turma, Periodo, Agenda
from turmas.serializers import TurmaSerializer, AgendaSerializer
from django.core import serializers

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

class TestesAgendaSerializer(TestCase):
    def testa_criacao_de_objeto(self):
        dados_corretos = {'nome': 'Trabalho 2',
            'tipo': 'Individual',
            'descricao': 'Descrição da agenda...'
        }
        dados_errados = {'nome': 'Trabalho 2',
            'tipo': 'teste',
            'descricao': 'Descrição da agenda...'
        }

        agenda = Agenda.objects.create(**dados_errados)
        serializer_correto = AgendaSerializer().create(dados_corretos)
        serializer_incorreto = AgendaSerializer(agenda, data=dados_errados)

        self.assertEqual(serializer_correto.nome,  'Trabalho 2')
        self.assertEqual(serializer_correto.tipo,  'Individual')
        self.assertEqual(serializer_correto.descricao, 'Descrição da agenda...')
        self.assertTrue(isinstance(serializer_correto, Agenda))
        self.assertFalse(serializer_incorreto.is_valid())
        self.assertEquals(set(serializer_incorreto.errors), set(['tipo']))