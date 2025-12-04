from django.db import models
from lagos.models import Lago

class Siembra(models.Model):
    lago = models.ForeignKey(Lago, on_delete=models.CASCADE)
    fecha_siembra = models.DateField()
    cantidad_peces = models.PositiveIntegerField()
    peso_promedio_inicial = models.DecimalField(max_digits=6, decimal_places=2)
    costo_por_pez = models.DecimalField(max_digits=8, decimal_places=2)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    observaciones = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.costo_total = self.cantidad_peces * self.costo_por_pez
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Siembra {self.fecha_siembra} - {self.lago.nombre}"
    

class Alimentacion(models.Model):
    lago = models.ForeignKey(Lago, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_alimento = models.CharField(max_length=100)
    cantidad_kg = models.DecimalField(max_digits=6, decimal_places=2)
    costo_por_kg = models.DecimalField(max_digits=8, decimal_places=2)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.costo_total = self.cantidad_kg * self.costo_por_kg
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.lago.nombre} - {self.fecha} - {self.hora}"
    

class Muestreo(models.Model):
    lago = models.ForeignKey(Lago, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad_muestreada = models.PositiveIntegerField(default=30)
    peso_total_kg = models.DecimalField(max_digits=8, decimal_places=2)
    peso_promedio = models.DecimalField(max_digits=6, decimal_places=3, editable=False)
    observaciones = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.cantidad_muestreada > 0:
            self.peso_promedio = self.peso_total_kg / self.cantidad_muestreada
        else:
            self.peso_promedio = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Muestreo {self.fecha} - {self.lago.nombre}"
    
class Venta(models.Model):
    lago = models.ForeignKey(Lago, on_delete=models.CASCADE)
    fecha = models.DateField()
    kilos_vendidos = models.DecimalField(max_digits=10, decimal_places=2)
    precio_por_kg = models.DecimalField(max_digits=10, decimal_places=2)
    ingreso_total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.ingreso_total = self.kilos_vendidos * self.precio_por_kg
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.fecha} - {self.lago.nombre}"