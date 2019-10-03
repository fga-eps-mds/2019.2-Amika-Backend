from django.db import models

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length = 100) 
    ano = models.IntegerField()                        
    periodo = models.IntegerField()  
