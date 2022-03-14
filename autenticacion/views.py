from django.shortcuts import render, redirect

# Create your views here.

def autenticacion(request):
    return render(request,"autenticacion/autenticacion.html")
