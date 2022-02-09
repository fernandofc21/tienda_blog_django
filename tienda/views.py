from django.shortcuts import render
from tienda.models import CategoriaProducto, Producto

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request,"tienda/tienda.html", {"productos":productos})