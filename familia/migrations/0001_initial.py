# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('talla', models.IntegerField(help_text='Talla en cm')),
                ('peso', models.IntegerField(help_text='Ingrese lbs')),
                ('otro', models.TextField(help_text='Cuales son tus intereses')),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
    ]
