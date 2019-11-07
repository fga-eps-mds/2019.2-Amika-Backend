from django.test import TestCase

from amika import serializers
from amika.serializers import *
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class TestesRegistroSerializer(TestCase):
    def setUp(self):
        Turma.objects.create(descricao="A")

    def testa_cria_registro(self):
        registro_dados = {
            'matricula': 123456789,
            'turma': 'A'
        }

        serializer = RegistroSerializer().create(registro_dados)
        self.assertTrue(isinstance(serializer, Registro))

    def testa_turma_nao_existe(self):
        registro_dados = {
            'matricula': 123456789,
            'turma': 'B'
        }

        serializer = RegistroSerializer(data=registro_dados)
        serializer.is_valid()
        self.assertEqual(serializer.errors['turma'][0], 'Turma não encontrada.')


class TestesAlunoSerializer(TestCase):
    def setUp(self):
        Registro.objects.create(
            matricula=123456789,
            turma=Turma.objects.create(descricao="A"),
            periodo=Periodo.objects.create(ano=2019, semestre=2))

        Grupo.objects.create(nome="Feliz")

    def testa_criacao_de_aluno(self):
        aluno_dados = {
            'username': '123456789',
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'password': "123",
            'grupo': 'Feliz'
        }

        serializer = AlunoSerializer().create(aluno_dados)
        self.assertTrue(isinstance(serializer, Aluno))

    def testa_atualizacao_de_aluno(self):
        aluno = Aluno.objects.create(
            username='123456789',
            first_name='Nome',
            last_name='Sobrenome',
            password='123',
            registro=Registro.objects.first())

        alteracao = {
            'password': '123456',
            'grupo': 'Feliz',
            'formulario': [{'tipo': 'A', 'pontuacao': 10}],
            'foto': '/media/abc.png',
        }

        serializer = AlunoSerializer().update(aluno, alteracao)
        self.assertTrue(isinstance(serializer, Aluno))

    def testa_atualizacao_de_aluno_com_formulario_existente(self):
        formulario = Formulario.objects.create(tipo='A', pontuacao=10.00)

        aluno = Aluno.objects.create(
            username='123456789',
            first_name='Nome',
            last_name='Sobrenome',
            password='123',
            registro=Registro.objects.first())
        aluno.formulario.add(formulario)
        aluno.save()

        alteracao = {
            'formulario': [{'tipo': 'A', 'pontuacao': 20.00}]
        }

        serializer = AlunoSerializer().update(aluno, alteracao)
        self.assertTrue(isinstance(serializer, Aluno))

    def testa_grupo_nao_existe(self):
        aluno_dados = {
            'username': '123456789',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': '123',
            'grupo': 'Felicidade'
        }

        serializer = AlunoSerializer(data=aluno_dados)
        serializer.is_valid()
        self.assertEqual(serializer.errors['grupo'][0], 'Grupo não encontrado.')

    def testa_grupo_existente(self):
        aluno_dados = {
            'username': '123456789',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': '123',
            'grupo': 'Feliz',
            'formulario': None,
            'foto': None,
        }

        serializer = AlunoSerializer(data=aluno_dados)
        serializer.is_valid()
        self.assertEqual(serializer.data, aluno_dados)


class TestesAgendaSerializer(TestCase):
    def teste_capitaliza_tipo(self):
        dados_agenda = {
            "nome": "Atividade 2",
            "descricao": "descricao agenda...",
            "tipo": "individual",
            "data_disponibilizacao": "2019-09-09",
            "data_encerramento": "2019-09-10"
        }

        serializer = AgendaSerializer(data=dados_agenda)
        serializer.is_valid()
        self.assertEqual(serializer.initial_data['tipo'], "Individual")

    def teste_data_encerramento_maior_que_data_disponibilizacao(self):
        dados_agenda = {
            "nome": "Atividade 2",
            "descricao": "descricao agenda...",
            "tipo": "individual",
            "data_disponibilizacao": "2019-09-09",
            "data_encerramento": "2019-09-08"
        }

        serializer = AgendaSerializer(data=dados_agenda)
        serializer.is_valid()
        self.assertEqual(serializer.errors['error'][0], "Data de disponibilização maior do que a de encerramento.")


class TestesHumor(TestCase):
    def testa_criacao_de_humor_do_dia(self):
        humor_do_dia = {
            "humor_do_dia": "3",
            "aluno": "2",
            "data": "2019-10-10"
        }

        serializer = HumorSerializer().create(humor_do_dia)
        self.assertTrue(isinstance(serializer, Humor))

    def testa_raises_validation_error(self):
        humor_do_dia = {
            "humor_do_dia": "3",
            "aluno": "2"
        }

        serializer = HumorSerializer().create(humor_do_dia)
        if Humor.objects.filter(data=serializer.data, aluno=serializer.aluno):
            with self.assertRaises(serializers.ValidationError): HumorSerializer().create(humor_do_dia)
class TestesAgendaRealizarSerializer(TestCase):
    def testa_criacao_agenda_realizar(self):
        agenda1 = Agenda.objects.create(
            nome="Atividade 2",
            descricao="descricao agenda...",
            tipo="individual",
            data_disponibilizacao="2019-09-09",
            data_encerramento="2019-09-08")
        
        with open('arquivos/banner.png', 'rb') as tratadorArquivo:
            anexo = tratadorArquivo.read()

        arquivo = SimpleUploadedFile("banner.png", anexo, content_type="file")
        self.client.post(reverse('enviar_anexo'), {'anexo': arquivo})

        dados_agenda = {
            'texto': 'Resposta...',
            'anexo': arquivo,
            'agenda_id': agenda1.id
        }

        serializer = AgendaRealizarSerializer(data=dados_agenda)
        self.assertTrue(serializer.is_valid(), isinstance(serializer, AgendaRealizar))
    
    def testa_atualizacao_agenda_realizar(self):
        with open('arquivos/anexo.txt', 'rb') as tratadorArquivo:
            anexo = tratadorArquivo.read()

        arquivo = SimpleUploadedFile("anexo.txt", anexo, content_type="file")
        self.client.post(reverse('enviar_anexo'), {'anexo': arquivo})

        agenda2 = AgendaRealizar.objects.create(
            texto='Resposta',
            anexo=arquivo,
            agenda=Agenda.objects.create(
                nome="Atividade 2",
                descricao="descricao agenda...",
                tipo="Individual",
                data_disponibilizacao="2019-09-09",
                data_encerramento="2019-09-10"
            ))

        agenda_id = AgendaRealizar.objects.first().pk

        dados_alteracao = {
            'texto': 'Resposta nova',
            'agenda_id': agenda_id
        }

        serializer = AgendaRealizarSerializer().update(agenda2, dados_alteracao)
        self.assertTrue(isinstance(serializer, AgendaRealizar))