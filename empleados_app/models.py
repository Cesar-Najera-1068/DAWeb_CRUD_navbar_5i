from django.db import models

# Create your models here.


class Empleados(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    Nombres=models.CharField(max_length=50)
    Apellidos=models.CharField(max_length=50)
    Numerotelefono=models.CharField(max_length=50)
    Horario=models.CharField(max_length=50)
    Correoelectronico=models.CharField(max_length=10)
    Salario=models.CharField(max_length=10)

    def __str__(self) :
        return self.Nombres