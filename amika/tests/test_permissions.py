from unittest.mock import MagicMock

from django.contrib.auth.models import AnonymousUser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from amika.permissions import Permissoes
from amika.views import *


class TetesPermissoes(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.admin = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.grupo = Grupo.objects.create(nome='Felicidade')
        self.aluno = Aluno.objects.create(username='123456789',
                                          first_name='Nome',
                                          last_name='Sobrenome',
                                          password='123456789',
                                          registro=Registro.objects.create(
                                              matricula='123456789',
                                              turma=Turma.objects.create(descricao='A'),
                                              periodo=Periodo.objects.create(ano=2019, semestre=2)),
                                          grupo=self.grupo)
        self.agenda = Agenda.objects.create(nome="Atividade 2",
                                            descricao="descricao agenda...",
                                            tipo="individual",
                                            data_disponibilizacao="2019-09-09",
                                            data_encerramento="2019-09-10")
        self.material = Material.objects.create(arquivo=SimpleUploadedFile("file.mp4",
                                                                           b"file_content",
                                                                           content_type="video/mp4"))
        self.agenda_realizada = AgendaRealizada.objects.create(texto="Resposta atividade 2",
                                                               agenda=self.agenda,
                                                               aluno=self.aluno)

    def testa_post_aluno(self):
        content = {
            'username': '123456789',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': '123',
            'grupo': None,
            'formulario': None,
        }
        request = self.factory.post(reverse('post_aluno'), content, content_type='application/json')
        request.user = AnonymousUser()
        self.assertTrue(Permissoes().has_permission(request, post))

    def testa_get_aluno(self):
        request = self.factory.get(reverse('rud_aluno', kwargs={'pk': self.aluno.pk}))
        request.user = self.admin
        request.parser_context = {'kwargs': {'pk': self.aluno.pk}}
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_put_aluno(self):
        request = self.factory.put(reverse('rud_aluno', kwargs={'pk': self.aluno.pk}))
        request.user = self.aluno
        request.parser_context = {'kwargs': {'pk': self.aluno.pk}}
        self.assertTrue(Permissoes().has_permission(request, rud))

    def testa_get_grupo(self):
        request = self.factory.get(reverse('rud_grupo', kwargs={'pk': self.grupo.pk}))
        request.user = self.aluno
        request.parser_context = {'kwargs': {'pk': self.grupo.pk, 'username': self.aluno.username}}
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_get_agendas(self):
        request = self.factory.get(reverse('get_agendas'))
        request.user = self.admin
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_get_agenda(self):
        request = self.factory.get(reverse('rud_agenda', kwargs={'pk': self.agenda.pk}))
        request.user = self.admin
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_get_materiais(self):
        request = self.factory.get(reverse('get_materiais'))
        request.user = self.admin
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_get_material(self):
        request = self.factory.get(reverse('rud_material', kwargs={'pk': self.material.pk}))
        request.user = self.admin
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_post_agenda_realizada(self):
        content = {
            'texto': 'Agenda realizada',
            'agenda': self.agenda.id,
            'aluno': self.aluno.id,
        }
        request = self.factory.post(reverse('post_agenda_realizada'), content, content_type='application/json')
        request.user = self.admin
        self.assertTrue(Permissoes().has_permission(request, post))

    def testa_get_agenda_realizada(self):
        request = self.factory.get(reverse('rud_agenda_realizada', kwargs={'pk': self.agenda_realizada.pk}))
        request.user = self.aluno
        request.parser_context = {'kwargs': {'pk': self.agenda_realizada.pk}}
        self.assertTrue(Permissoes().has_permission(request, rud))

    def testa_get_agendas_realizadas_aluno(self):
        request = self.factory.get(reverse('get_agendas_realizadas_aluno', kwargs={'pk': self.aluno.pk}))
        request.user = self.aluno
        request.parser_context = {'kwargs': {'pk': self.aluno.pk}}
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_get_agendas_nao_realizadas_aluno(self):
        request = self.factory.get(reverse('get_agendas_nao_realizadas_aluno', kwargs={'pk': self.aluno.pk}))
        request.user = self.aluno
        request.parser_context = {'kwargs': {'pk': self.aluno.pk}}
        self.assertTrue(Permissoes().has_permission(request, get))

    def testa_put_agenda_realizada(self):
        request = self.factory.put(reverse('rud_agenda_realizada', kwargs={'pk': self.agenda_realizada.pk}))
        request.user = self.aluno
        request.parser_context = {'kwargs': {'pk': self.agenda_realizada.pk}}
        self.assertTrue(Permissoes().has_permission(request, rud))
