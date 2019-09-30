from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cadastrar_usuario.views import RegistrosMultiplosViewSet, cadastrar_aluno

class TestUrls(SimpleTestCase):

    def test_set_registration_list_resolves(self):
        url = reverse('set_registration_list')
        self.assertEquals(resolve(url).func.view_class, RegistrosMultiplosViewSet)

    def test_cadastrar_aluno_resolves(self):
        url = reverse('cadastrar_aluno')
        self.assertEquals(resolve(url).func, cadastrar_aluno)
