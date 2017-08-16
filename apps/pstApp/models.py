# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

trayecto = (('1','1',),('2','2'),('3','3'),('4','4'))
trimestre = (('I','I'),('II','II'),('III','III'),('IV','IV'))
fase = (('I','Incio'),('II','Elaboracion'),('III','Construccion'),('IV','Transicion'))
ponderacion = (('A','5'),('B','4'),('C','3'),('D','2'),('E','1'))

@python_2_unicode_compatible
class universidad(models.Model):
	nombre_universidad = models.CharField(max_length=100, null=False, blank=False)
	logo = models.ImageField(upload_to='logosUniversidades/%Y/%m/%d', verbose_name='logosUniversidades')
	rif = models.CharField(max_length=16, null=False, blank=False)
	telefono = models.CharField(max_length=16, null=False, blank=False)
	email_universidad = models.EmailField(max_length=100)
	direccion = models.TextField(max_length=400)
	
	def __str__(self):
		return '%i --> %s' % (self.id, self.nombre_universidad)

@python_2_unicode_compatible
class docentes(models.Model):
	cedula = models.CharField(max_length=8, unique=True, primary_key=True)
	area_saber = models.CharField(max_length=60, null=False, blank=False)
	celular = models.CharField(max_length=13, blank=False)
	profesion = models.CharField(max_length=60, null=False, blank=False)
	id_universidad = models.ForeignKey('universidad', null=True, blank=True)
	usuario_id = models.ForeignKey(User, null=True, blank=True)
	
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
	comunidad_institucion = models.TextField(max_length=200)
	estado = models.CharField(max_length=30, null=False, blank=False)
	ciudad = models.CharField(max_length=30, null=False, blank=False)
	municipio = models.CharField(max_length=30, null=False, blank=False)
	id_grupo = models.ForeignKey('grupo', null=True, blank=True)

	def __str__(self):
		return '%i' % (self.id)

@python_2_unicode_compatible
class avances(models.Model):
	actividadrevisada = models.TextField(max_length=1200)
	actividadasignada = models.TextField(max_length=1200)
	observaciones = models.TextField(max_length=1200)
	fechaproxentrega = models.DateField(null=False, blank=False)
	id_proyecto = models.ForeignKey('proyecto',null=True, blank=True)
	
	def __str__(self):
		return 'Avance: %i' % (self.id)

@python_2_unicode_compatible
class pregunta(models.Model):
	fase = models.CharField(max_length=10, choices=fase)
	Trayecto = models.CharField(max_length=4, choices=trayecto)
	trimestre = models.CharField(max_length=4, choices=trimestre)
	item = models.CharField(max_length=160, null=False, blank=False)
	
	def __str__(self):
		return 'Id. Pregunta: %i' % (self.id)

class evaluacionGrupal(models.Model):
	puntos = models.CharField(max_length=4, choices=ponderacion)
	id_preguntas = models.ForeignKey('pregunta', null=True, blank=True)
	id_grupo = models.ForeignKey('grupo', null=True, blank=True)
	
	def __str__(self):
		return 'Grupo: %i' % (self.id_grupo)

class evaluacionIndividual(models.Model):
	puntosIndividual = models.CharField(max_length=4, choices=ponderacion)
	id_preguntas = models.ForeignKey('pregunta', null=True, blank=True)
	id_estudiante = models.ForeignKey('estudiantes', null=True, blank=True)

	def __str__(self):
		return 'id. Estudiante: %i' % (self.id_estudiante)
