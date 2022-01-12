from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Inicio')



def services(request):
    return HttpResponse('Servicios')

def marketplace(request):
    return HttpResponse('Tienda')

def blog(request):
    return HttpResponse('Servicios')

def contact(request):
    return render(request,"contacto.html")