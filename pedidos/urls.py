from django.urls import path
from pedidos.views import procesar_pedido
from tienda.views import tienda

from django.conf import settings


urlpatterns = [
    path('', procesar_pedido, name="pedido"),
]

