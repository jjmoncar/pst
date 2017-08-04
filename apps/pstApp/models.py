# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

trayecto = (('1','1',),('2','2'),('3','3'),('4','4'))
trimestre = (('I','I'),('II','II'),('III','III'),('IV','IV'))

@python_2_unicode_compatible
class docentes(models.Model):
	cedula = models.CharField(max_length=8, unique=True, primary_key=True)
	nombre = models.CharField(max_length=40, null=False, blank=False)
	apellido = models.CharField(max_length=60, null=False, blank=False)
	area_saber = models.CharField(max_length=60, null=False, blank=False)
	celular = models.CharField(max_length=13, blank=False)
	correo = models.EmailField(max_length=100)
	profesion = models.CharField(max_length=60, null=False, blank=False)
	
	def __str__(self):
		return '%s --> %s, %s' % (self.cedula, self.nombre, self.apellido)

@python_2_unicode_compatible	
class estudiantes(models.Model):
	cedula_est = models.CharField(max_length=8, unique=True, primary_key=True)
	nombre_est = models.CharField(max_length=40, null=False, blank=False)
	apellido_est = models.CharField(max_length=60, null=False, blank=False)
	seccion = models.CharField(max_length=4, null=False, blank=False)
	trayecto = models.CharField(max_length=4, choices=trayecto)
	trimestre = models.CharField(max_length=4, choices=trimestre)
	id_docente = models.ForeignKey('docentes', null=True, blank=True)
	
	def __str__(self):
		return '%s --> %s, %s' % (self.cedula_est, self.nombre_est, self.apellido_est)
	
class grupo(models.Model):
	num_grupo = models.IntegerField(null=False, blank=False)
	id_estudiante = models.ForeignKey('estudiantes', null=True, blank=True)
	
	def __str__(self):
		return 'Grupo: %i' % (self.num_grupo)
	
@python_2_unicode_compatible
class proyecto(models.Model):
	nombre_proy = models.TextField(max_length=300)
	id_grupo = models.ForeignKey('grupo', null=True, blank=True)

	def __str__(self):
		return '%i' % (self.id)
