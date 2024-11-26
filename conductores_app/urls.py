from django.urls import path
from conductores_app import views
urlpatterns = [
    path("conductores", views.inicio_vistaConductores, name="conductores"),
    path("registrarConductor/",views.registrarConductor,name="registrarConductor"),
    path("seleccionarConductor/<id_conductor>",views.seleccionarConductor,name="seleccionarConductor"),
    path("editarConductor/",views.editarConductor,name="editarConductor"),
    path("borrarConductor/<id_conductor>",views.borrarConductor,name="borrarConductor")
]