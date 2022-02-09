from django.urls import path
from tienda.views import tienda

from django.conf import settings


urlpatterns = [
    path('', tienda, name="tienda"),
]

