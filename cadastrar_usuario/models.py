from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
	matricula = models.charField(max_length=9)
	nome = models.charField(max_length=50)
	senha = models.charField(max_lenght=20)
	email = models.charField(max_lenght=40)

	def publish(self):
		self.save()