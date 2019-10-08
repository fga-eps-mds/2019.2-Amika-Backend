# Generated by Django 2.2.5 on 2019-10-02 01:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(choices=[(2019, 2019)])),
                ('semestre', models.IntegerField(choices=[(1, 1), (2, 2)])),
            ],
            options={
                'ordering': ['-ano', '-semestre'],
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('matricula', models.DecimalField(decimal_places=0, max_digits=9, primary_key=True, serialize=False)),
                ('turma', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='periodo', to='alunos.Periodo')),
            ],
            options={
                'ordering': ['turma', 'matricula'],
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('registro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alunos.Registro')),
            ],
            options={
                'ordering': ['username'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]