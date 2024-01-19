from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput
from .models import *

class TareaAdmin(admin.ModelAdmin):
    # Personaliza el nombre del campo en el panel de administración
    verbose_name = 'TareaPrincipal'

    # Personaliza la amplitud del campo en el panel de administración
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '400'})},
    } 
admin.site.register(Tarea,TareaAdmin)
admin.site.register(TareaIndividual)
admin.site.register(TareaPrincipal)
admin.site.register(Grupo)
admin.site.register(TrabGrupo)