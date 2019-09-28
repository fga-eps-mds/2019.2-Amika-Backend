from django.db import models
from django.conf import settings

# Create your models here.

class Aluno(models.Model):
	matricula = models.CharField(primary_key=True, max_length=9)
	nome = models.CharField(max_length=70)
	senha = models.CharField(max_length=400)
	email = models.CharField(max_length=50, unique=True)

class Registration(models.Model):
	matricula = models.CharField( max_length=9)
	turma = models.CharField(max_length=1)