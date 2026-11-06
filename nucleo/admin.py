from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Setor, Colaborador, Equipamento, Emprestimo

# Register your models here.
class SetorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Setor)
admin.site.register(Colaborador)
admin.site.register(Equipamento)
admin.site.register(Emprestimo)