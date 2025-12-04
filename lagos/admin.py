from django.contrib import admin
from .models import Lago

@admin.register(Lago)
class LagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'capacidad_maxima', 'fecha_registro')
    search_fields = ('nombre', 'ubicacion')