from django.db import models

# Create your models here.

class Camiones(models.Model):
    id_camion=models.CharField(primary_key=True,max_length=6)
    Matricula=models.CharField(max_length=50)
    Modelo=models.CharField(max_length=50)
    Marca=models.CharField(max_length=50)
    Capacidadpasajeros=models.CharField(max_length=50)
    Estadodelcamion=models.CharField(max_length=10)
    Tipodemotor=models.CharField(max_length=10)

    def __str__(self) :
        return self.Matricula