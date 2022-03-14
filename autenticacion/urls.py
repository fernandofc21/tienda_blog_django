from argparse import Namespace
from django.urls import path
from autenticacion.views import autenticacion

from django.conf import settings

##Asignando namespaces


urlpatterns = [
    path('', autenticacion, name="autenticacion"),
]

