# Generated by Django 2.2.5 on 2019-10-30 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amika', '0002_humor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='materiais/')),
            ],
        ),
    ]
