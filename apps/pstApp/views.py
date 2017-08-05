# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from .models import universidad, docentes, estudiantes, grupo, proyecto

class principal(TemplateView):
	template_name = 'template/principal.html'
	
class Inicio(TemplateView):
	template_name = 'template/index.html'
	
class AcercaDe(TemplateView):
	template_name = 'template/acercade.html'
