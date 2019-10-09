from django.db import models
from django.db.models import PROTECT
import datetime

class Turma(models.Model):
    nome = models.CharField(max_length = 100)         
    periodo = models.ForeignKey("Periodo", related_name='periodo', on_delete=PROTECT)

    def __str__(self):
        return "{} {}".format(self.nome, self.periodo)


class Periodo(models.Model):
    ano = models.IntegerField(choices=[(y, y) for y in range(2019, datetime.date.today().year + 1)])
    semestre = models.IntegerField(choices=[(1, 1), (2, 2)])

    def __str__(self):
        return "{}/{}".format(self.ano, self.semestre)

class Agenda(models.Model):
    nome = models.CharField(max_lenght = 100)
    desricao = models.CharField(max_lenght = 500) 
    tipo = models.BooleanField()
    data_disponibilizacao = models.DateField(default=datetime.now)

class Atividade(models.Model):
    data_entrega = models.DateField()
    texto = models.TextField(max_lenght = 500)
    arquivo = models.FileField()
    agenda = models.ForeignKey("Agenda", related_name='agenda')