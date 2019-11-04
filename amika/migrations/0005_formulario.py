# Generated by Django 2.2.5 on 2019-10-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amika', '0004_auto_20191104_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'ordering': ['tipo', 'pontuacao'],
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='formulario',
            field=models.ManyToManyField(blank=True, to='amika.Formulario'),
        ),
    ]