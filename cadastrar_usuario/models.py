from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
	matricula = models.CharField(max_length=9, blank=False, null=False)
	nome = models.CharField(max_length=50, blank=False, null=False)
	"""O tamanho do campo deve ser aumentado, pois por questões de segurança iremos 
	guardar o hash da senha criptografada e não a senha cadastrada"""
	senha = models.CharField(max_length=20, blank=False, null=False)
	email = models.CharField(max_length=40, blank=False, null=False)

	def publish(self):
		self.save()

class Registration(models.Model):
	matricula = models.CharField( max_length=9)
	turma = models.CharField(max_length=1)