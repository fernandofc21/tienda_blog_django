from django.urls import path
from ProyectoWebApp.views import home, contact, marketplace

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inicio', home, name="home"),
    path('tienda', marketplace, name="tienda"),
    path('contacto', contact, name="contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)