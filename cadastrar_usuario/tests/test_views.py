from django.test import TestCase, Client
from django.urls import reverse, include, path
# from cadastrar_usuario.models import Project, Category, Expense
import json
from rest_framework.test import APITestCase, URLPatternsTestCase
from cadastrar_usuario.views import MultipleRegistrationsViewSet
from rest_framework import status
from django.views import generic
from test_plus.test import CBVTestCase

class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('cadastrar_usuario.urls')),
    ]

    def test_cadastrar_aluno(self):
        url = reverse('cadastrar_aluno')
        data = {
            "matricula_aluno": "123456",
            "nome_aluno": "teste",
            "senha_aluno": "123",
            "email_aluno": "new@email.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(response.data, data)

class MultipleRegistrationsViewTest(TestCase):

    def setUp(self):

        self.url = reverse('set_registration_list')

    def test_response_200_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_response_200_post(self):
        data = {
            'matricula': '123456789',
            'turma': 'a'
        }
        response = self.client.post(self.url, data, format='json')
        """Retire o id antes de testar o dado que chega, pois o id é adicionado automaticamente e 
        não precisamos verificar ele."""
        response.data.pop('id')
        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)