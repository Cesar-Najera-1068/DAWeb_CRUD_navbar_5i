from django.urls import path
from central_app import views
urlpatterns = [
    path("viajes", views.inicio_vistaViajes, name="viajes"),
    path("registrarViaje/",views.registrarViaje,name="registrarViaje"),
    path("seleccionarViaje/<id_viaje>",views.seleccionarViaje,name="seleccionarViaje"),
    path("editarViaje/",views.editarViaje,name="editarViaje"),
    path("borrarViaje/<id_viaje>",views.borrarViaje,name="borrarViaje")
]