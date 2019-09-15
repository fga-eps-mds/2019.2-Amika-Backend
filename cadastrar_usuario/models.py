from django.db import models
from django.conf import settings

# Create your models here.

class UsuarioAluno(models.Model):
	matricula_aluno = models.CharField(max_length=9)
	nome_aluno = models.CharField(max_length=50)
	senha_aluno = models.CharField(max_length=20)
	email_aluno = models.CharField(max_length=40)
