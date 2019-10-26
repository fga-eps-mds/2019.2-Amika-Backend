# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
#
# from amika.views import cadastra_registro, lista_registros, remove_registro, cadastra_aluno, lista_alunos, \
#     cadastra_turma, lista_turmas, gerencia_turma
#
#
# class TestesUrls(SimpleTestCase):
#     def testa_url_cadastra_registro(self):
#         self.assertEquals(resolve(reverse('cadastra_registro')).func, cadastra_registro)
#
#     def testa_url_lista_registros(self):
#         self.assertEquals(resolve(reverse('lista_registros')).func, lista_registros)
#
#     def testa_url_remove_registro(self):
#         self.assertEquals(resolve(reverse('remove_registro', kwargs={'matricula': 123456789})).func, remove_registro)
#
#     def testa_url_cadastra_aluno(self):
#         self.assertEquals(resolve(reverse('cadastra_aluno')).func, cadastra_aluno)
#
#     def testa_url_lista_alunos(self):
#         self.assertEquals(resolve(reverse('lista_alunos')).func, lista_alunos)
#
#
#     def testa_url_cadastra_turma(self):
#         self.assertEquals(resolve(reverse('cadastra_turma')).func, cadastra_turma)
#
#     def testa_url_lista_turmas(self):
#         self.assertEquals(resolve(reverse('lista_turmas')).func, lista_turmas)
#
#     def testa_url_gerencia_turma(self):
#         self.assertEquals(resolve(reverse('gerencia_turma', kwargs={"pk": 1})).func, gerencia_turma)
