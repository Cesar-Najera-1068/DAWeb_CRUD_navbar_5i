from django.urls import path
from app_base import views

urlpatterns = [
        #Inicio centralcamion
    path('', views.inicio),
]
