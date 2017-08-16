# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UniversidadForm(forms.ModelForm):
	class Meta:
		model = universidad
		fields = [
			'nombre_universidad',
			'logo',
			'rif',
			'telefono',
			'email_universidad',
			'direccion',
		]
		labels = {
			'nombre_universidad': 'Nombre',
			'logo': 'Logo',
			'rif': 'R.I.F',
			'telefono': 'Telefono',
			'email_universidad': 'Email',
			'direccion': 'Dirección',
		}

class DocenteForm(forms.ModelForm):
	class Meta:
		model = docentes
		fields = [
			'cedula',
			'area_saber',
			'celular',
			'profesion',
			'id_universidad',
		]
		labels = {
			'cedula': 'Cedula',
			'area_saber': 'Saber',
			'celular': 'Celular',
			'profesion': 'Profesion',
			'id_universidad': 'Universidad',
		}

class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo',
		}
