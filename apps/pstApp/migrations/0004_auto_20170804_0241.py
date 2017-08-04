# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-04 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pstApp', '0003_auto_20170803_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='universidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_universidad', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logosUniversidades/%Y/%m/%d', verbose_name='logosUniversidades')),
                ('rif', models.CharField(max_length=16)),
                ('telefono', models.CharField(max_length=16)),
                ('email_universidad', models.EmailField(max_length=100)),
                ('direccion', models.TextField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='docentes',
            name='id_universidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pstApp.universidad'),
        ),
    ]
