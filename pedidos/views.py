from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carrito.carrito import Carrito
from django.contrib import messages
from pedidos.models import LineaPedido, Pedido

# Create your views here.
@login_required(login_url="/autenticacion/iniciar_sesion")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carrito(request)
    lineas_pedido=list()
    for key, value in carro.carrito.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido= pedido

        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)
        
    
    messages.success(request, "Pedido creado correctamente")

    return redirect("../tienda/")