# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pstApp', '0002_grupo_num_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='num_grupo',
            field=models.IntegerField(),
        ),
    ]