from django.db import models

class Patrimonio(models.Model):  # Creación de clase llamada Patrimonio (models.Model = modelo de Django)

    nombre = models.CharField(max_length=100)  # Texto más pequeño de máximo 100 letras.
    descripcion = models.TextField()  # Texto más largo
    ubicacion = models.CharField(max_length=150) 
    precio = models.IntegerField()  # Número Entero
    filtro_estudiante = models.BooleanField(default=False)  # True o False (por defecto falso)
    comida_cerca = models.BooleanField(default=False)
    horario = models.CharField(max_length=200)

    def __str__(self):  # OPCIONAL, solo para que en /admin cada patrimonio se vea con su nombre y no "Patrimonio object"
        return self.nombre