from django.urls import path
from ProyectoWebApp.views import home, services, blog, contact, marketplace

urlpatterns = [
    path('inicio', home, name="home"),
    path('servicios', services, name="servicios"),
    path('tienda', marketplace, name="tienda"),
    path('blog', blog, name="blog"),
    path('contacto', contact, name="contacto"),
]