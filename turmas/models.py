from django.db import models
from django.db.models import PROTECT
from datetime import datetime, date

class Turma(models.Model):
    nome = models.CharField(max_length = 100)         
    periodo = models.ForeignKey("Periodo", related_name='periodo', on_delete=PROTECT)

    def __str__(self):
        return "{} {}".format(self.nome, self.periodo)


class Periodo(models.Model):
    ano = models.IntegerField(choices=[(y, y) for y in range(2019, date.today().year + 1)])
    semestre = models.IntegerField(choices=[(1, 1), (2, 2)])

    def __str__(self):
        return "{}/{}".format(self.ano, self.semestre)

class Agenda(models.Model):
    TIPO_CHOICES = (
        ("Individual", "Individual"), 
        ("Grupo", "Grupo"),
    )
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 500) 
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data_disponibilizacao = models.DateField(default=datetime.now)
    data_encerramento = models.DateField()

class Atividade(models.Model):
    data_entrega = models.DateField()
    texto = models.TextField(max_length = 500)
    arquivo = models.FileField()
    agenda = models.ForeignKey("Agenda", related_name='agenda', on_delete=PROTECT)