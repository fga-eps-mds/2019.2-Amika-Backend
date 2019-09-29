from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from turmas.views import Turma
from turmas.serializers import TurmaSerializer
import json

class TurmaViewsCasosdeTeste(TestCase):
    cliente = APIClient()

    def criar_turma(self):
        turma = Turma.objects.create(
            nome_turma = "Felicidade",
            ano_turma = 2019,
            periodo_turma = 2
        )
        return turma

    def testa_listar_turmas_GET(self):
        resposta = self.cliente.get(reverse('lista_turmas'))
        self.assertEquals(resposta.status_code, 200)

    def testa_criar_turmas_POST(self):
        resposta = self.cliente.post(reverse('cria_turmas'), {
            'nome_turma':'Felicidade',
            'ano_turma':'2019',
            'periodo_turma':'2'
        }, format='json')
        self.assertEquals(resposta.status_code, 200)

    def testa_get_turma_GET(self):
        turma = self.criar_turma()
        id = turma.pk
        resposta = self.client.get(reverse('mostra_turma', args = [id]))
        self.assertEquals(resposta.status_code, 200)

    def testa_editar_turma_PUT(self):
        turma = self.criar_turma()
        id = turma.pk
        resposta = self.cliente.put(reverse('edita_turma', args = [id]))
        self.assertEquals(resposta.status_code, 200)

    def testa_deletar_turmas_DELETE(self):
        turma = self.criar_turma()
        id = turma.pk
        resposta = self.cliente.delete(reverse('deleta_turma', args = [id]))
        self.assertEquals(resposta.status_code, 200)


