from django.shortcuts import render
from django.http.response import HttpResponse

from carrito.carrito import Carrito


# Create your views here.

def home(request):

    carrito = Carrito(request)
    
    return render(request,"ProyectoWebApp/home.html")

def marketplace(request):
    return render(request,"ProyectoWebApp/tienda.html")
