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

    # Relatórios
    path('relatorios/emprestimos', views.rel_emprest, name='rel-emprest'),
]
