import json

from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO

from amika.views import *


class TestesGet(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='admin', is_staff=True)
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.authorization = 'JWT {}'.format(response.data['token'])

    def testa_retorna_objetos(self):
        response = self.client.get(reverse('get_registros'), HTTP_AUTHORIZATION=self.authorization)
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

        response = self.client.get(reverse('popula_grupos'), HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testa_agendas_realizadas_aluno(self):
        response = self.client.get(reverse('get_agendas_realizadas_aluno', kwargs={'pk': 2}),
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testa_agendas_nao_realizadas_aluno(self):
        response = self.client.get(reverse('get_agendas_nao_realizadas_aluno', kwargs={'pk': 2}),
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestesPost(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='admin', is_staff=True)
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.authorization = 'JWT {}'.format(response.data['token'])

    def testa_request_sem_dados(self):
        content = {}
        response = self.client.post(reverse('post_registro'), json.dumps(content), content_type='application/json',
                                    HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testa_aluno_nao_registrado(self):
        content = {
            "username": "123",
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "password": "123"
        }
        response = self.client.post(reverse('post_aluno'), json.dumps(content), content_type='application/json',
                                    HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_cadastra_registo(self):
        Turma.objects.create(descricao='A')

        content = [{
            "matricula": "123456789",
            "turma": "A"
        }]
        response = self.client.post(reverse('post_registro'), json.dumps(content), content_type='application/json',
                                    HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_cadastra_turma(self):
        content = {"descricao": "A"}
        response = self.client.post(reverse('post_turma'), json.dumps(content), content_type='application/json',
                                    HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_nao_cadastra_turma_com_erro(self):
        content = {"nome": "A"}
        response = self.client.post(reverse('post_turma'), json.dumps(content), content_type='application/json',
                                    HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestesRud(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='admin', is_staff=True)
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.authorization = 'JWT {}'.format(response.data['token'])

        Turma.objects.create(descricao='A')

    def teste_nao_tem_objeto(self):
        response = self.client.get(reverse('rud_turma', kwargs={'pk': 100}),
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def teste_visualiza_turma(self):
        response = self.client.get(reverse('rud_turma', kwargs={'pk': Turma.objects.first().pk}),
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_edita_turma(self):
        response = self.client.put(reverse('rud_turma', kwargs={'pk': Turma.objects.first().pk}),
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_deleta_turma(self):
        response = self.client.delete(reverse('rud_turma', kwargs={'pk': Turma.objects.first().pk}),
                                      HTTP_AUTHORIZATION=self.authorization)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
