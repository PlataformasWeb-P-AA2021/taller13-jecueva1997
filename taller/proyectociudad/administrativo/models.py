from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo = (
        ('residencial', 'Tipo residencial'),
        ('comercial', 'Tipo comercial'),
    )
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo_edificio = models.CharField(max_length=30, \
        choices=opciones_tipo)

    def __str__(self):
        return "%s " % (self.nombre)

    
                            

class Departamento(models.Model):
    nombre_prop = models.CharField("Nombre del Propietario", max_length=100)
    costo_depart = models.DecimalField("Costo de departamentos", max_digits=100, decimal_places=2)
    numero_cuartos = models.IntegerField("Número de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="edificios")

    def __str__(self):
        return "%s %s" % (self.nombre_prop, self.numero_cuartos)

    
