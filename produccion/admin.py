from django.contrib import admin
from .models import Siembra, Alimentacion, Muestreo, Venta

@admin.register(Siembra)
class SiembraAdmin(admin.ModelAdmin):
    list_display = ('lago', 'fecha_siembra', 'cantidad_peces', 'peso_promedio_inicial', 'costo_total')
    list_filter = ('lago', 'fecha_siembra')


@admin.register(Alimentacion)
class AlimentacionAdmin(admin.ModelAdmin):
    list_display = ('lago', 'fecha', 'hora', 'tipo_alimento', 'cantidad_kg', 'costo_total')
    list_filter = ('lago', 'fecha', 'tipo_alimento')

@admin.register(Muestreo)
class MuestreoAdmin(admin.ModelAdmin):
    list_display = ('lago', 'fecha', 'cantidad_muestreada', 'peso_total_kg', 'peso_promedio')
    list_filter = ('lago', 'fecha')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('lago', 'fecha', 'kilos_vendidos', 'precio_por_kg', 'ingreso_total')
    list_filter = ('lago', 'fecha')