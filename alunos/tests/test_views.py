from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from alunos.models import Registro, Periodo


class TestesAluno(TestCase):
    def setUp(self) -> None:
        Registro.objects.create(
            matricula=123456789,
            turma="A",
            periodo=Periodo.objects.create(
                ano=2019,
                semestre=2))

    def testa_cadastra_de_aluno(self):
        aluno_dados = {
            'username': '123456789',
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'password': "123"
        }
        response = self.client.post(reverse('cadastra_aluno'), aluno_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_nao_cadastra_aluno_sem_dados(self):
        aluno_dados = {}
        response = self.client.post(reverse('cadastra_aluno'), aluno_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_nao_cadastra_aluno_com_falta_de_dados(self):
        aluno_dados = {
            'username': '123456789',
            'first_name': "Nome",
            'last_name': "Sobrenome",
            # 'password': "123"
        }
        response = self.client.post(reverse('cadastra_aluno'), aluno_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_nao_cadastra_aluno_nao_registrado(self):
        aluno_dados = {
            'username': '123',
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'password': "123"
        }
        response = self.client.post(reverse('cadastra_aluno'), aluno_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestesRegistro(TestCase):
    def teste_cadastra_registros_sem_erros(self):
        registro_dados = [{
            "matricula": 123456781,
            "turma": "A"
        }]
        response = self.client.post(reverse('cadastra_registro'), registro_dados, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_cadastra_registros_com_erros(self):
        registro_dados = [
            {
                "matricula": 123456781,
                "turma": "A"
            },
            {
                "matricula": 123456781,
                "turma": "A"
            },
            {
                "matricula": 123456782,
                "turma": "A"
            }
        ]
        response = self.client.post(reverse('cadastra_registro'), registro_dados, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_nao_cadastra_registro_sem_dados(self):
        registro_dados = {}
        response = self.client.post(reverse('cadastra_registro'), registro_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_remove_registro(self):
        Registro.objects.create(
            matricula=123456789,
            turma="A",
            periodo=Periodo.objects.create(
                ano=2019,
                semestre=2))

        response = self.client.delete(reverse('remove_registro', kwargs={'matricula': 123456789}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def teste_nao_remove_registro(self):
        response = self.client.delete(reverse('remove_registro', kwargs={'matricula': 123456789}), format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestesListaObjetos(TestCase):
    def teste_lista_alunos(self):
        response = self.client.get(reverse('lista_objetos', kwargs={'tipo': 'alunos'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def teste_lista_registros(self):
        response = self.client.get(reverse('lista_objetos', kwargs={'tipo': 'registros'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def teste_nao_lista_objetos_diferentes(self):
        response = self.client.get(reverse('lista_objetos', kwargs={'tipo': 'foo'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
