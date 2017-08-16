# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pstApp', '0006_avances'),
    ]

    operations = [
        migrations.CreateModel(
            name='evaluacionGrupal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.CharField(choices=[('A', '5'), ('B', '4'), ('C', '3'), ('D', '2'), ('E', '1')], max_length=4)),
                ('id_grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pstApp.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='evaluacionIndividual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntosIndividual', models.CharField(choices=[('A', '5'), ('B', '4'), ('C', '3'), ('D', '2'), ('E', '1')], max_length=4)),
                ('id_estudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pstApp.estudiantes')),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fase', models.CharField(choices=[('I', 'Incio'), ('II', 'Elaboracion'), ('III', 'Construccion'), ('IV', 'Transicion')], max_length=10)),
                ('Trayecto', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=4)),
                ('trimestre', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], max_length=4)),
                ('item', models.CharField(max_length=160)),
            ],
        ),
        migrations.AddField(
            model_name='evaluacionindividual',
            name='id_preguntas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pstApp.pregunta'),
        ),
        migrations.AddField(
            model_name='evaluaciongrupal',
            name='id_preguntas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pstApp.pregunta'),
        ),
    ]