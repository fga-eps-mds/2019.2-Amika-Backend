from django.test import SimpleTestCase
from django.urls import reverse, resolve

from alunos.views import cadastra_aluno, cadastra_registro, remove_registro, lista_objetos


class TestesUrls(SimpleTestCase):
    def testa_url_cadastra_aluno(self):
        self.assertEquals(resolve(reverse('cadastra_aluno')).func, cadastra_aluno)

    def testa_url_cadastra_registro(self):
        self.assertEquals(resolve(reverse('cadastra_registro')).func, cadastra_registro)

    def testa_url_remove_registro(self):
        self.assertEquals(resolve(reverse('remove_registro', kwargs={'matricula': 123456789})).func, remove_registro)

    def testa_url_lista_objetos_alunos(self):
        self.assertEquals(resolve(reverse('lista_objetos', kwargs={'tipo': 'alunos'})).func, lista_objetos)

    def testa_url_lista_registros(self):
        self.assertEquals(resolve(reverse('lista_objetos', kwargs={'tipo': 'registros'})).func, lista_objetos)
