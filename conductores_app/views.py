from django.shortcuts import render,redirect
from .models import Conductores

def inicio_vistaConductores(request):
    losconductores=Conductores.objects.all()
    return render(request,"gestionarConductores.html",{"misconductores":losconductores})

def registrarConductor(request):
    id_conductor=request.POST["txtidconductor"]
    Nombres=request.POST["txtnombres"]
    Apellidos=request.POST["txtapellidos"]
    Numerolicencia=request.POST["txtlicen"]
    Horario=request.POST["txthorario"]
    Numerotelefono=request.POST["txtnumtele"]
    Correoelectronico=request.POST["txtcorreo"]
    
    guardarconductor=Conductores.objects.create(id_conductor=id_conductor, Nombres=Nombres, Apellidos=Apellidos,Numerolicencia=Numerolicencia ,Numerotelefono=Numerotelefono, Horario=Horario, Correoelectronico=Correoelectronico)

    return redirect("conductores")

def seleccionarConductor(request, id_conductor):
    conductores=Conductores.objects.get(id_conductor=id_conductor)
    return render(request,"editarConductores.html",{"misconductores": conductores})

def editarConductor(request):
    id_conductor=request.POST["txtidconductor"]
    Nombres=request.POST["txtnombres"]
    Apellidos=request.POST["txtapellidos"]
    Numerolicencia=request.POST["txtlicen"]
    Horario=request.POST["txthorario"]
    Numerotelefono=request.POST["txtnumtele"]
    Correoelectronico=request.POST["txtcorreo"]
    conductor=Conductores.objects.get(id_conductor=id_conductor)
    conductor.Nombres=Nombres
    conductor.Apellidos=Apellidos
    conductor.Numerotelefono=Numerotelefono
    conductor.Horario=Horario
    conductor.Correoelectronico=Correoelectronico
    conductor.Numerolicencia=Numerolicencia
    conductor.save()
    return redirect("conductores")

def borrarConductor(request,id_conductor):
    conductor=Conductores.objects.get(id_conductor=id_conductor)
    conductor.delete()
    return redirect("conductores")