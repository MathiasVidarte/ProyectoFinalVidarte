

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Camiseta(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    talla = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"
