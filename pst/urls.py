"""pst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.pstApp.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(Inicio.as_view()), name='Inicio'),
    url(r'^accounts/login/', login, {'template_name':'template/index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^principal/', login_required(principal.as_view()), name='principal'),
    url(r'^acercade/', login_required(AcercaDe.as_view()), name='acercade'),
    
    #URLs Universidad
    url(r'^nuevaUniversidad/', login_required(universidadCreate.as_view()), name='nuevaUniversidad'),
    url(r'^universidadListar/', login_required(universidadListar.as_view()), name='universidadListar'),
    url(r'^universidadEditar/(?P<pk>\d+)/', login_required(universidadEditar.as_view()), name='universidadEditar'),
]
