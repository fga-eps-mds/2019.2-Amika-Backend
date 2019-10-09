from django.test import TestCase
from grupos.models import Grupo

class TestesGrupo(TestCase):
    def setUp(self):
        Grupo.objects.create(nome="Grupo 1")

    def testa_str_do_objeto(self):
        self.assertEqual(str(Grupo.objects.first()), "Grupo 1")