from django.urls import path
from camiones_app import views
urlpatterns = [
    path("camiones", views.inicio_vistaCamiones, name="camiones"),
    path("registrarCamion/",views.registrarCamion,name="registrarCamion"),
    path("seleccionarCamion/<id_camion>",views.seleccionarCamion,name="seleccionarCamion"),
    path("editarCamion/",views.editarCamion,name="editarCamion"),
    path("borrarCamion/<id_camion>",views.borrarCamion,name="borrarCamion")
]