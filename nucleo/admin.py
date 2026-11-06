from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Setor

# Register your models here.
class SetorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Setor, SetorAdmin)