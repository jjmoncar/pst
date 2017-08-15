# -*- coding: utf-8 -*-

from django import forms
from .models import universidad

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
