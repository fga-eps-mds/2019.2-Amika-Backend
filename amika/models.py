from datetime import datetime, date
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import PROTECT, CASCADE


class Periodo(models.Model):
    ano = models.PositiveSmallIntegerField(choices=[(y, y) for y in range(date.today().year, date.today().year + 1)])
    semestre = models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2)])

    class Meta:
        unique_together = ['ano', 'semestre']
        ordering = ['-ano', '-semestre']

    def __str__(self):
        return "{}/{}".format(self.ano, self.semestre)


class Turma(models.Model):
    descricao = models.CharField(unique=True, max_length=2)

    def __str__(self):
        return self.descricao


class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    tipo = models.CharField(max_length=10, choices=[['Individual', 'Individual'], ['Grupo', 'Grupo']])
    data_disponibilizacao = models.DateField(default=datetime.now)
    data_encerramento = models.DateField()

    def __str__(self):
        return "{} {} {}/{}".format(self.nome, self.tipo, self.data_disponibilizacao, self.data_encerramento)


class Grupo(models.Model):
    nome = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.nome


class Registro(models.Model):
    matricula = models.CharField(max_length=9, validators=[RegexValidator(regex='^\\d{9}$')])
    turma = models.ForeignKey(Turma, on_delete=PROTECT)
    periodo = models.ForeignKey(Periodo, on_delete=PROTECT)

    class Meta:
        unique_together = ['matricula', 'periodo']
        ordering = ['-periodo', 'turma', 'matricula']

    def __str__(self):
        return "{} {} {}".format(self.periodo, self.turma, self.matricula)


class Aluno(User):
    registro = models.OneToOneField(Registro, on_delete=CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT, null=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return "{} {}".format(self.username, self.get_full_name())


class Humor(models.Model):
    humor_do_dia = models.IntegerField()
    aluno = models.IntegerField()
    data = models.DateField(default=datetime.now)

    def __str__(self):
        return "{} {} {}".format(self.humor_do_dia, self.data, self.aluno)


class Material(models.Model):
    arquivo = models.FileField(upload_to='materiais/')

    def __str__(self):
        return self.arquivo.name
