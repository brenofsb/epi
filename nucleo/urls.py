"""
URL configuration for epi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [

    # Colaboradores
    path('', views.home, name='nucleo-inicial'),
    path('criar', views.tela_criar, name='nucleo-criar'),
    path('salvar', views.salvar, name='nucleo-salvar'),
    path('editar/<int:id>', views.editar, name='nucleo-editar'),
    path('excluir/<int:id>', views.excluir, name='nucleo-excluir'),

    # Equipamentos
    path('equipamentos', views.equipa, name='equipa'),
    path('equipamento/criar', views.equipa_criar, name='equipa-criar'),
    path('equipamento/salvar', views.equipa_salvar, name='equipa-salvar'),
    path('equipamento/editar/<int:id>', views.equipa_editar, name='equipa-editar'),
    path('equipamento/excluir/<int:id>', views.equipa_excluir, name='equipa-excluir'),

    # Emprestimos
    path('emprestimo/criar', views.emprest_criar, name='emprestimo-criar'),
    path('emprestimos', views.emprest_listar, name='emprest-listar'),
    path('emprestimo/editar/<int:id>', views.emprest_editar, name='emprest-editar'),
]
