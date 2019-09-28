# Generated by Django 2.2.5 on 2019-09-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('senha', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('matricula', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('turma', models.CharField(max_length=1)),
            ],
        ),
    ]
