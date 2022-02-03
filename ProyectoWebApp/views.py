from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def home(request):
    return render(request,"ProyectoWebApp/home.html")

def marketplace(request):
    return render(request,"ProyectoWebApp/tienda.html")

def contact(request):
    return render(request,"ProyectoWebApp/contacto.html")