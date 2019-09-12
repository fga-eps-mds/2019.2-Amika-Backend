from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
	matricula = models.CharField(max_length=9)
	nome = models.CharField(max_length=50)
	senha = models.CharField(max_length=20)
	email = models.CharField(max_length=40)

	def publish(self):
		self.save()

