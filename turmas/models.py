from django.db import models

# Create your models here.

class Turma(models.Model):
    nome_turma = models.CharField(max_length = 100) 
    ano_turma = models.IntegerField()                        
    periodo_turma = models.IntegerField()  
    id_turma = models.IntegerField(primary_key=True)  
