# Generated by Django 2.2.5 on 2019-10-25 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amika', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Humor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humor_do_dia', models.IntegerField()),
                ('aluno', models.IntegerField()),
                ('data', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]