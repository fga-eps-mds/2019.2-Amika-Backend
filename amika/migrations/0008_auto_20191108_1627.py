# Generated by Django 2.2.5 on 2019-11-08 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amika', '0007_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amika.Grupo'),
        ),
    ]
