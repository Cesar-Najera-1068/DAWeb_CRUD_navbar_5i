from django.shortcuts import render,redirect
from .models import Camiones
# Create your views here.

def inicio_vistaCamiones(request):
    loscamiones=Camiones.objects.all()
    return render(request,"gestionarCamiones.html",{"miscamiones":loscamiones})

def registrarCamion(request):
    id_camion=request.POST["txtidcamion"]
    Matricula=request.POST["txtmatricula"]
    Modelo=request.POST["txtmodelo"]
    Marca=request.POST["txtmarca"]
    Capacidadpasajeros=request.POST["txtpasajeros"]
    Estadodelcamion=request.POST["txtestado"]
    Tipodemotor=request.POST["txtmotor"]
    
    guardarcamion=Camiones.objects.create(id_camion=id_camion, Matricula=Matricula, Modelo=Modelo, Marca=Marca, Capacidadpasajeros=Capacidadpasajeros, Estadodelcamion=Estadodelcamion, Tipodemotor=Tipodemotor)

    return redirect("camiones")

def seleccionarCamion(request, id_camion):
    camiones=Camiones.objects.get(id_camion=id_camion)
    return render(request,"editarCamiones.html",{"miscamiones": camiones})

def editarCamion(request):
    id_camion=request.POST["txtidcamion"]
    Matricula=request.POST["txtmatricula"]
    Modelo=request.POST["txtmodelo"]
    Marca=request.POST["txtmarca"]
    Capacidadpasajeros=request.POST["txtpasajeros"]
    Estadodelcamion=request.POST["txtestado"]
    Tipodemotor=request.POST["txtmotor"]
    camion=Camiones.objects.get(id_camion=id_camion)
    camion.Matricula=Matricula
    camion.Modelo=Modelo
    camion.Marca=Marca
    camion.Capacidadpasajeros=Capacidadpasajeros
    camion.Estadodelcamion=Estadodelcamion
    camion.Tipodemotor=Tipodemotor
    camion.save()
    return redirect("camiones")

def borrarCamion(request,id_camion):
    camion=Camiones.objects.get(id_camion=id_camion)
    camion.delete()
    return redirect("camiones")