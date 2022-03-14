from argparse import Namespace
from django.urls import path
from carrito.views import agregar_producto, eliminar_producto, limpiar_carro, restar_producto

from django.conf import settings

##Asignando namespaces

app_name="carrito"

urlpatterns = [
    path('agregar/<producto_id>/', agregar_producto, name="agregar"),
    path('eliminar/<producto_id>/', eliminar_producto, name="eliminar"),
    path('restar/<producto_id>/', restar_producto, name="restar"),
    path('limpiar/', limpiar_carro, name="limpiar"),
]

