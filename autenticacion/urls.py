from argparse import Namespace
from django.urls import path
from .views import VRegistro

from django.conf import settings

##Asignando namespaces


urlpatterns = [
    path('', VRegistro.as_view(), name="autenticacion"),
]

