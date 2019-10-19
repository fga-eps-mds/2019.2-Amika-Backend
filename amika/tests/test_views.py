from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from amika.models import *


class TesteGet(TestCase):
    def testa_retorna_objetos(self):
        response = self.client.get(reverse('get_registros'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testa_popula_grupos(self):
        periodo = Periodo.objects.create(ano=2019, semestre=2)
        turma = Turma.objects.create(descricao="A")

        for i in range(100000000, 100000031):
            Aluno.objects.create(
                username=str(i),
                first_name='Nome',
                last_name='Sobrenome',
                password='123',
                registro=Registro.objects.create(matricula=str(i), turma=turma, periodo=periodo))

        response = self.client.get(reverse('popula_grupos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPost(TestCase):
    def testa_request_sem_dados(self):
        dados = {}
        response = self.client.post(reverse('post_registro'), dados, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testa_aluno_nao_registrado(self):
        aluno_dados = {
            'username': '123',
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'password': "123"
        }
        response = self.client.post(reverse('post_aluno'), aluno_dados, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_cadastra_registo(self):
        Turma.objects.create(descricao='A')

        registro_dados = [{
            'matricula': '123456789',
            'turma': 'A'
        }]
        response = self.client.post(reverse('post_registro'), registro_dados, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_cadastra_turma(self):
        turma_dado = {
            'descricao': 'A'
        }
        response = self.client.post(reverse('post_turma'), turma_dado, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_nao_cadastra_turma_com_erro(self):
        turma_dado = {
            'nome': 'A'
        }
        response = self.client.post(reverse('post_turma'), turma_dado, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TesteRud(TestCase):
    def setUp(self):
        Turma.objects.create(descricao='A')

    def teste_nao_tem_objeto(self):
        response = self.client.get(reverse('rud_turma', kwargs={'pk': 100}))
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def teste_visualiza_turma(self):
        response = self.client.get(reverse('rud_turma', kwargs={'pk': Turma.objects.first().pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_edita_turma(self):
        response = self.client.put(reverse('rud_turma', kwargs={'pk': Turma.objects.first().pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_deleta_turma(self):
        response = self.client.delete(reverse('rud_turma', kwargs={'pk': Turma.objects.first().pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
