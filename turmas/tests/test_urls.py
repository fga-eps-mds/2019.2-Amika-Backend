from django.test import SimpleTestCase
from django.urls import reverse, resolve
from turmas.views import gerencia_turmas, gerencia_turma

class TesteUrls(SimpleTestCase):
    def testa_url_gerencia_turmas(self):
        url = reverse('gerencia_turmas')
        self.assertEquals(resolve(url).func, gerencia_turmas)

    def testa_url_gerencia_turma(self):
        url = reverse('gerencia_turma', args=[1])
        self.assertEquals(resolve(url).func, gerencia_turma)