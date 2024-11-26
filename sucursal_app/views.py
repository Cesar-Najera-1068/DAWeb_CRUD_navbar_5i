from django.shortcuts import render,redirect
from .models import Sucursales

def inicio_vistaSucursales(request):
    lossucursales=Sucursales.objects.all()
    return render(request,"gestionarSucursales.html",{"missucursales":lossucursales})

def registrarSucursal(request):
    id_sucursal=request.POST["txtidsucursal"]
    Nombre=request.POST["txtnombre"]
    Direccion=request.POST["txtdireccion"]
    Numerotelefono=request.POST["txtnumtel"]
    Correoelectronico=request.POST["txtcorreo"]
    Horario=request.POST["txthorario"]
    Paginaweb=request.POST["txtpagina"]
    
    guardarsucursal=Sucursales.objects.create(id_sucursal=id_sucursal, Nombre=Nombre, Direccion=Direccion, Numerotelefono=Numerotelefono, Horario=Horario, Correoelectronico=Correoelectronico, Paginaweb=Paginaweb)

    return redirect("sucursales")

def seleccionarSucursal(request, id_sucursal):
    sucursales=Sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request,"editarSucursal.html",{"missucursales": sucursales})

def editarSucursal(request):
    id_sucursal=request.POST["txtidsucursal"]
    Nombre=request.POST["txtnombre"]
    Direccion=request.POST["txtdireccion"]
    Numerotelefono=request.POST["txtnumtel"]
    Correoelectronico=request.POST["txtcorreo"]
    Horario=request.POST["txthorario"]
    Paginaweb=request.POST["txtpagina"]
    sucursal=Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.Nombre=Nombre
    sucursal.Direccion=Direccion
    sucursal.Numerotelefono=Numerotelefono
    sucursal.Horario=Horario
    sucursal.Correoelectronico=Correoelectronico
    sucursal.Paginaweb=Paginaweb
    sucursal.save()
    return redirect("sucursales")

def borrarSucursal(request,id_sucursal):
    sucursal=Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursales")