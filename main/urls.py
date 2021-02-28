from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('servicios/', ServicioList.as_view(), name='servicio-list'),
    path('servicios/crear', ServicioCreate.as_view(), name='servicio-create'),
    path('servicios/detalle/<pk>', ServicioDetail.as_view(), name='servicio-detail'),
    path('servicios/modificar/<pk>', ServicioUpdate.as_view(), name='servicio-update'),
    path('servicios/eliminar/<pk>', ServicioDelete.as_view(), name='servicio-delete'),
    path('clientes/', ClienteList.as_view(), name='cliente-list'),
    path('clientes/crear', ClienteCreate.as_view(), name='cliente-create'),
    path('clientes/detalle/<pk>', ClienteDetail.as_view(), name='cliente-detail'),
    path('clientes/modificar/<pk>', ClienteUpdate.as_view(), name='cliente-update'),
    path('clientes/eliminar/<pk>', ClienteDelete.as_view(), name='cliente-delete'),
    path('motores/', MotorList.as_view(), name='motor-list'),
    path('motores/crear', MotorCreate.as_view(), name='motor-create'),
    path('motores/detalle/<pk>', MotorDetail.as_view(), name='motor-detail'),
    path('motores/modificar/<pk>', MotorUpdate.as_view(), name='motor-update'),
    path('motores/eliminar/<pk>', MotorDelete.as_view(), name='motor-delete'),
]
