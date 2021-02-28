from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('servicios/', ServicioList.as_view(), name='servicio-list'),
    path('servicios/crear', ServicioCreate.as_view(), name='servicio-create'),
    path('servicios/detalle/<slug:slug>', ServicioDetail.as_view(), name='servicio-detail'),
    path('servicios/modificar/<slug:slug>', ServicioUpdate.as_view(), name='servicio-update'),
    path('servicios/eliminar/<slug:slug>', ServicioDelete.as_view(), name='servicio-delete'),
]
