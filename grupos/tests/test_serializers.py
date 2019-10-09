from django.test import TestCase
from grupos.models import Grupo
from grupos.serializers import GrupoSerializer

class TestesGrupoSerializer(TestCase):
    def testa_criacao_de_objeto(self):
        grupo_dados = {
            'nome':'Grupo'
        }

        grupo = GrupoSerializer().create(grupo_dados)
        self.assertTrue(isinstance(grupo, Grupo))