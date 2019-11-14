from datetime import datetime, date

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import PROTECT, CASCADE, SET_NULL


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

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    tipo = models.CharField(max_length=10, choices=[['Individual', 'Individual'], ['Grupo', 'Grupo']])
    data_disponibilizacao = models.DateField(default=datetime.now)
    data_encerramento = models.DateField()

    class Meta:
        ordering = ['-data_encerramento', '-data_disponibilizacao', 'tipo', 'nome', 'descricao']

    def __str__(self):
        return "{} {} {}/{}".format(self.nome, self.tipo, self.data_disponibilizacao, self.data_encerramento)


class Grupo(models.Model):
    nome = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Formulario(models.Model):
    tipo = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    pontuacao = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['tipo', 'pontuacao']

    def __str__(self):
        return "{} {}".format(self.tipo, self.pontuacao)


class Registro(models.Model):
    matricula = models.CharField(max_length=9, validators=[RegexValidator(regex='^\\d{9}$')])
    turma = models.ForeignKey(Turma, on_delete=PROTECT)
    periodo = models.ForeignKey(Periodo, on_delete=PROTECT)

    class Meta:
        unique_together = ['matricula', 'periodo']
        ordering = ['-periodo', 'turma', 'matricula']

    def __str__(self):
        return "{} {} {}".format(self.periodo, self.turma, self.matricula)


def aluno_foto_diretorio(instance, filename):
    return '{}/foto_perfil/{}'.format(instance.aluno.username, filename)


class Aluno(User):
    registro = models.OneToOneField(Registro, on_delete=CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=SET_NULL, null=True)
    formulario = models.ManyToManyField(Formulario, blank=True)
    foto = models.ImageField(upload_to=aluno_foto_diretorio, null=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return "{} {}".format(self.username, self.get_full_name())


def aluno_agenda_realizada_diretorio(instance, filename):
    return '{}/agenda_realizada/{}'.format(instance.aluno.username, filename)


class AgendaRealizada(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    data_ultima_alteracao = models.DateField(auto_now_add=True)
    texto = models.TextField()
    anexo = models.FileField(upload_to=aluno_agenda_realizada_diretorio, null=True)
    agenda = models.ForeignKey(Agenda, on_delete=CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=CASCADE)

    class Meta:
        unique_together = ['agenda', 'aluno']
        ordering = ['agenda__nome', '-data_ultima_alteracao', '-data_criacao', 'aluno__username']

    def __str__(self):
        return "{} {} {}".format(self.aluno.username, self.agenda.nome, self.data_ultima_alteracao)


class Humor(models.Model):
    humor_do_dia = models.IntegerField()
    aluno = models.IntegerField()
    data = models.DateField(default=datetime.now)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return "{} {} {}".format(self.humor_do_dia, self.data, self.aluno)


class Material(models.Model):
    arquivo = models.FileField(upload_to='materiais/')

    class Meta:
        ordering = ['arquivo__nome']

    def __str__(self):
        return self.arquivo.name