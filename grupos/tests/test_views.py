from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from grupos.models import Grupo
from grupos.views import popula_grupos


class TestesGrupo(TestCase):
    def setUp(self):
        Grupo.objects.create(nome='Grupo 1')

    def teste_cadastra_grupo(self):
        grupo_dados = {"nome": "Grupo 2"}
        response = self.client.post(reverse('cria_grupo'), grupo_dados, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def teste_nao_cadastra_grupo_sem_dados(self):
        grupo_dado_incompletos = {}
        response = self.client.post(reverse('cria_grupo'), grupo_dado_incompletos, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_nao_cadastra_grupo_com_dados_errados(self):
        grupo_dado_errado = {"nome": True}
        response = self.client.post(reverse('cria_grupo'), grupo_dado_errado, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def teste_visualiza_grupos(self):
        response = self.client.get(reverse('lista_grupos'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_visualiza_grupo(self):
        response = self.client.get(reverse('gerencia_grupo', kwargs={'pk': Grupo.objects.first().pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_nao_visualiza_grupo(self):
        response = self.client.get(reverse('gerencia_grupo', kwargs={'pk': 2}))
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def teste_edita_grupo(self):
        response = self.client.put(reverse('gerencia_grupo', kwargs={'pk': Grupo.objects.first().pk}),
                                   content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_deleta_grupo(self):
        response = self.client.delete(reverse('gerencia_grupo', kwargs={'pk': Grupo.objects.first().pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def teste_aloca_alunos(self):
        response = popula_grupos()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
