from django.db import models

# Create your models here.


class Sucursales(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=50)
    Numerotelefono=models.CharField(max_length=50)
    Correoelectronico=models.CharField(max_length=50)
    Horario=models.CharField(max_length=10)
    Paginaweb=models.CharField(max_length=10)

    def __str__(self) :
        return self.Nombre