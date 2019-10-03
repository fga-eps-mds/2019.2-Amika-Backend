from django.db import models
from django.db.models import PROTECT
import datetime

class Turma(models.Model):
    nome = models.CharField(max_length = 100)         
    periodo = models.ForeignKey("Periodo", related_name='periodo', on_delete=PROTECT)

class Periodo(models.Model):
    ano = models.IntegerField(choices=[(y, y) for y in range(2019, datetime.date.today().year + 1)])
    semestre = models.IntegerField(choices=[(1, 1), (2, 2)])