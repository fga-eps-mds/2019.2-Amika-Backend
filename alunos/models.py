import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import PROTECT, CASCADE


class Aluno(User):
    registro = models.OneToOneField("Registro", on_delete=CASCADE)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return "{} {}".format(self.username, self.get_full_name())


class Registro(models.Model):
    matricula = models.DecimalField(primary_key=True, max_digits=9, decimal_places=0)
    turma = models.CharField(max_length=1, choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")])
    periodo = models.ForeignKey("Periodo", related_name='periodo', on_delete=PROTECT)

    class Meta:
        ordering = ['turma', 'matricula']

    def __str__(self):
        return "{} {} {}".format(self.turma, self.matricula, self.periodo)


class Periodo(models.Model):
    ano = models.IntegerField(choices=[(y, y) for y in range(2019, datetime.date.today().year + 1)])
    semestre = models.IntegerField(choices=[(1, 1), (2, 2)])

    class Meta:
        ordering = ['-ano', '-semestre']

    def __str__(self):
        return "{}/{}".format(self.ano, self.semestre)
