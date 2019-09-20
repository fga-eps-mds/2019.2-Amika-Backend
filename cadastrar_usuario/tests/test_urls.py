from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cadastrar_usuario.views import tela_de_cadastro, MultipleRegistrationsViewSet

class TestUrls(SimpleTestCase):

    def test_initial_screen_resolves(self):
        url = reverse('tela_de_cadastro')
        self.assertEquals(resolve(url).func, tela_de_cadastro)

    def test_set_registration_list_resolves(self):
        url = reverse('set_registration_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, MultipleRegistrationsViewSet)
