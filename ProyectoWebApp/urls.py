from django.urls import path
from ProyectoWebApp.views import home, services, blog, contact, marketplace

urlpatterns = [
    path('inicio', home),
    path('servicios', services),
    path('tienda', marketplace),
    path('blog', blog),
    path('contacto/', contact),
]