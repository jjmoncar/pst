# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(universidad)
admin.site.register(docentes)
admin.site.register(estudiantes)
admin.site.register(grupo)
admin.site.register(proyecto)
admin.site.register(avances)
admin.site.register(pregunta)
admin.site.register(evaluacionGrupal)
admin.site.register(evaluacionIndividual)
