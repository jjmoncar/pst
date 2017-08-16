# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from .models import *
from .forms import *

class principal(TemplateView):
	template_name = 'template/principal.html'
	
class Inicio(TemplateView):
	template_name = 'template/index.html'
	
class AcercaDe(TemplateView):
	template_name = 'template/acercade.html'

#VIEWS del modelo universidad
class universidadCreate(CreateView):
	model = universidad
	template_name = 'template/universidad_form.html'
	form_class = UniversidadForm
	success_url = reverse_lazy('principal')

class universidadListar(ListView):
	model = universidad
	template_name = 'template/universidad_listar.html'
	paginate_by = 5

class universidadEditar(UpdateView):
	model = universidad
	template_name = 'template/universidad_form.html'
	form_class = UniversidadForm
	success_url = reverse_lazy('universidadListar')

#VIEWS registro de Usuarios
class RegistrarUsuario(CreateView):
	model = User
	template_name = 'template/registrarUsuario.html'
	form_class = RegistroForm
	second_form_class = DocenteForm
	success_url = reverse_lazy('principal')
	
	def get_context_data(self, **kwargs):
		context = super(RegistrarUsuario, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context
		
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			usuario = form.save(commit=False)
			usuario.perfil = form2.save()
			usuario.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))
	
class usuario_list(ListView):
	model = docentes
	template_name = 'template/usuario_listar.html'
	paginate_by = 4
	
class UsuarioUpdate(UpdateView):
	model = User
	template_name = 'template/registrarUsuario.html'
	form_class = RegistroForm
	success_url = reverse_lazy('principal')
