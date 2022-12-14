from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    nacimiento = models.CharField(max_length=100)
    

    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.nacimiento}, {self.id}"


class Dymmy(models.Model):

  nombre = models.CharField(max_length=100)

class Mascota(models.Model):

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.CharField(max_length=100)
    

    def __str__(self):
      return f"{self.nombre}, {self.raza}, {self.edad}, {self.id}"

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    dia = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    def __str__(self):
      return f"{self.nombre},{self.dia}, {self.horario}, {self.id}"