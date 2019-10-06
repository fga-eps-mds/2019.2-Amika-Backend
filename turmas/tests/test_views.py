from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from turmas.models import Turma, Periodo

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