from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cadastrar_usuario.views import set_registration_list, tela_de_cadastro

class TestUrls(SimpleTestCase):

    def test_initial_screen_resolves(self):
        url = reverse('tela_de_cadastro')
        self.assertEquals(resolve(url).func, tela_de_cadastro)

    def test_set_registration_list_resolves(self):
        url = reverse('set_registration_list')
        self.assertEquals(resolve(url).func, set_registration_list)
