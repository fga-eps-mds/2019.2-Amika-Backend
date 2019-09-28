from django.test import SimpleTestCase
from django.urls import reverse, resolve
from turmas.views import listar_turmas, criar_turmas, deletar_turma, editar_turma
from turmas.models import Turma

class TurmaUrlsCasosDeTestes(SimpleTestCase):
    def testa_lista_turmas(self):
        url = reverse('lista_turmas')
        self.assertEquals(resolve(url).func, listar_turmas)

    def testa_cria_turmas(self):
        url = reverse('cria_turmas')
        self.assertEquals(resolve(url).func, criar_turmas)

    def testa_deleta_turma(self):
        url = reverse('deleta_turma', args = [1])
        self.assertEquals(resolve(url).func, deletar_turma)

    def testa_edita_turma(self):
         url = reverse('edita_turma', args = [1])
         self.assertEquals(resolve(url).func, editar_turma)
