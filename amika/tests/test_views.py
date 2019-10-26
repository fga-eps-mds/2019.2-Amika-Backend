from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from amika.models import *

def criar_aluno(self, username, password, turma, periodo):
    
    self.user = Aluno.objects.create(username=username, 
                                    first_name='Nome', last_name="Sobrenome",
                                        registro=Registro.objects.create(
                                                    matricula=username, turma=turma, 
                                                    periodo=periodo
                                                )
                                    )
    self.user.set_password(password)
    self.user.save()

def criar_administrador(self, username, password):
    self.user = User.objects.create_user(username=username, email='', password=password, is_superuser=True)

def criar_dados_usuario(self, username, password):
    self.dados_usuario = {
        "username": username,
        "password": password
    }

def criar_turma(descricao):
    return Turma.objects.create(descricao=descricao)


def criar_periodo(ano, semestre):
    return Periodo.objects.create(ano=ano, semestre=semestre)

def get_token(self):
    self.url = reverse('login')
    response = self.client.post(reverse('login'), self.dados_usuario, format='json')
    try:
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION= self.token)
    except:
        self.token = ""
        self.client.credentials(HTTP_AUTHORIZATION= self.token)

class TeteAutenticacao(APITestCase):

    def testa_autenticacao(self):
        periodo = criar_periodo(2020,2)
        turma = criar_turma('B')
        criar_aluno(self, '130126721', 'senha', turma, periodo)
        criar_dados_usuario(self, '130126721', 'senha')
        get_token(self)
        verification_url = reverse('verificar-chave')
        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def testa_autenticacao_token_errado(self):
        verification_url = reverse('verificar-chave')
        resp = self.client.post(verification_url, {'token': 'token_errado'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def testa_autenticacao_usuario_errado(self):
        periodo = criar_periodo(2020,2)
        turma = criar_turma('B')
        criar_aluno(self, '130126721', 'senha', turma, periodo)
        criar_dados_usuario(self, '130129348', 'senha')
        get_token(self)
        verification_url = reverse('verificar-chave')
        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def testa_autenticacao_senha_errada(self):
        criar_dados_usuario(self, '130126721', 'senha_errada')
        get_token(self)
        verification_url = reverse('verificar-chave')
        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def testa_sem_autenticacao(self):
        response = self.client.get(reverse('get_registros'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def testa_chave_sem_permissao(self):
        periodo = criar_periodo(2020,2)
        turma = criar_turma('B')
        criar_aluno(self, 'aluno', 'senha_aluno', turma, periodo)
        criar_dados_usuario(self, 'aluno', 'senha_aluno')
        get_token(self)
        response = self.client.get(reverse('get_registros'), {'token': self.token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TesteGet(APITestCase):
    def setUp(self):
        criar_administrador(self, 'admin', 'senha')
        criar_dados_usuario(self, 'admin', 'senha')
        get_token(self)

    def testa_retorna_objetos(self):
        response = self.client.get(reverse('get_registros'), {'token': self.token}, format='json')
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


    def testa_perfil_aluno(self):
        periodo = criar_periodo(2020,2)
        turma = criar_turma('B')
        criar_aluno(self, "123456789", "senha", turma, periodo)
        criar_dados_usuario(self, '123456789', 'senha')
        get_token(self)
        response = self.client.get(reverse('perfil_usuario', kwargs={'pk':self.user.id}), {'token': self.token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPost(APITestCase):
    def setUp(self):
        criar_administrador(self, 'admin', 'senha_admin')
        criar_dados_usuario(self, 'admin', 'senha_admin')
        get_token(self)


    def testa_request_sem_dados(self):
        dados = {}
        response = self.client.post(reverse('post_registro'), dados)
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
        turma = Turma.objects.create(descricao='A')
        registro_dados = {
            "matricula": "123456789",
            "turma": "A"
        }
        response = self.client.post(reverse('post_registro'), registro_dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_cadastra_turma(self):
        turma_dado = {
            'descricao': 'A'
        }
        response = self.client.post(reverse('post_turma'), turma_dado)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_nao_cadastra_turma_com_erro(self):
        turma_dado = {
            'nome': 'A'
        }
        response = self.client.post(reverse('post_turma'), turma_dado, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TesteRud(APITestCase):
    def setUp(self):
        criar_administrador(self, 'admin', 'senha_admin')
        criar_dados_usuario(self, 'admin', 'senha_admin')
        get_token(self)
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
