from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from turmas.models import Turma, Periodo, Agenda

class TestesGerenciaDeTurmas(TestCase):
    def teste_cadastro_turma(self):
        turma_dados = {
            "nome": "Felicidade",
            "ano": 2019,
            "semestre": 2
        }   

        response = self.client.post(reverse('gerencia_turmas'), turma_dados, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def teste_cadastro_turma_com_dados_incompletos(self):
        turma_dados_incompletos = {
            "ano": 2019,
            "semestre": 2
        }      
        response = self.client.post(reverse('gerencia_turmas'), turma_dados_incompletos, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_visualizacao_turmas(self):
        response = self.client.get(reverse('gerencia_turmas'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

  
class TestesGerenciaDeTurma(TestCase):        
    def teste_visualizacao_turma(self): 
        turma = Turma.objects.create(
            nome = "Felicidade",
            periodo = Periodo.objects.create(ano=2019, semestre=2)
        )
        id = turma.id
        response = self.client.get(reverse('gerencia_turma', args = [id]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_edicao_turma(self):
        turma = Turma.objects.create(
            nome = "Felicidade",
            periodo = Periodo.objects.create(ano=2019, semestre=2)
        )
        id = turma.id
        response = self.client.put(reverse('gerencia_turma', args = [id]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_remocao_turma(self):
        turma = Turma.objects.create(
            nome = "Felicidade",
            periodo = Periodo.objects.create(ano=2019, semestre=2)
        )
        id = turma.id
        response = self.client.delete(reverse('gerencia_turma', args = [id]))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
class TestesGerenciaDeAgendas(TestCase):
    def teste_criacao_agenda(self):
        dados_agenda = {
            "nome": "Atividade 8",
            "descricao": "descricao agenda...",
            "tipo": "Individual",
            "data_disponibilizacao": "2019-09-09",
            "data_encerramento": "2019-09-10"
        }

        response = self.client.post(reverse('gerencia_agendas'), dados_agenda, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_visualizacao_agendas(self):
        response = self.client.get(reverse('gerencia_agendas'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

class TestesGerenciaDeAgenda(TestCase):
    def setUp(self):
        Agenda.objects.create(
            nome="Atividade 2",
            descricao="descrição da agenda...",
            tipo="Individual",
            data_disponibilizacao="2019-09-09",
            data_encerramento="2019-09-20"
        )
        self.dados_agenda = {
            "nome": "Atividade 2",
            "descricao": "descricao agenda...",
            "tipo": "Individual",
            "data_disponibilizacao": "2019-09-09",
            "data_encerramento": "2019-09-10"
        }
        self.id = Agenda.objects.first().id
    
    def teste_visualizazao_agenda(self):
        response = self.client.get(reverse('gerencia_agenda', args=[self.id]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_edicao_agendas(self):
        response = self.client.put(reverse('gerencia_agenda', args=[self.id]), data=self.dados_agenda, content_type = 'application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_remocao_agenda(self):
        response = self.client.delete(reverse('gerencia_agenda', args=[self.id]))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    