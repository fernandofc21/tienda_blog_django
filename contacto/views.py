from django.shortcuts import render, redirect
from contacto.forms import FormularioContacto
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    formulario_contacto = FormularioContacto()

    if request.method=="POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            send_mail(nombre, contenido, email, ['fercovic10@gmail.com'],)
            
            return redirect("/contacto/?valido")

    return render(request,"contacto/contacto.html", {"formulario":formulario_contacto})