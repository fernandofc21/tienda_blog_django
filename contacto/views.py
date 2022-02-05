from django.shortcuts import render
from contacto.forms import FormularioContacto
# Create your views here.

def contact(request):
    formulario_contacto = FormularioContacto()
    return render(request,"contacto/contacto.html", {"formulario":formulario_contacto})