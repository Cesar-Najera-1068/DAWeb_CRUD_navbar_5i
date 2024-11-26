from django.shortcuts import render,redirect
from .models import Empleados

def inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtidempleado"]
    Nombres=request.POST["txtnombres"]
    Apellidos=request.POST["txtapellidos"]
    Numerotelefono=request.POST["txtnumtel"]
    Horario=request.POST["txthorario"]
    Correoelectronico=request.POST["txtcorreoele"]
    Salario=request.POST["txtsalario"]
    
    guardarempleado=Empleados.objects.create(id_empleado=id_empleado, Nombres=Nombres, Apellidos=Apellidos, Numerotelefono=Numerotelefono, Horario=Horario, Correoelectronico=Correoelectronico, Salario=Salario)

    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleados.html",{"misempleados": empleados})

def editarEmpleado(request):
    id_empleado=request.POST["txtidempleado"]
    Nombres=request.POST["txtnombres"]
    Apellidos=request.POST["txtapellidos"]
    Numerotelefono=request.POST["txtnumtel"]
    Horario=request.POST["txthorario"]
    Correoelectronico=request.POST["txtcorreoele"]
    Salario=request.POST["txtsalario"]
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.Nombres=Nombres
    empleado.Apellidos=Apellidos
    empleado.Numerotelefono=Numerotelefono
    empleado.Horario=Horario
    empleado.Correoelectronico=Correoelectronico
    empleado.Salario=Salario
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request,id_empleado):
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")