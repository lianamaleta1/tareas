from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput
from .models import *

class NoticiaAdmin(admin.ModelAdmin):
    # Personaliza el nombre del campo en el panel de administración
    verbose_name = 'Noticias'

    # Personaliza la amplitud del campo en el panel de administración
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '400'})},
    } 
admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Documento)
admin.site.register(CategoriaDocumento)
admin.site.register(CategoriaIndicadores)
