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
