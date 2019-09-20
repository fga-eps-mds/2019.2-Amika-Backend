from django.db import models
from django.conf import settings

# Create your models here.

class UsuarioAluno(models.Model):
	matricula_aluno = models.CharField(primary_key=True, max_length=9)
	nome_aluno = models.CharField(max_length=70)
	senha_aluno = models.CharField(max_length=400)
	email_aluno = models.CharField(max_length=50, unique=True)

class Registration(models.Model):
	matricula = models.CharField(max_length=9)
	turma = models.CharField(max_length=1)