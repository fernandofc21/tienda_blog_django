from django.urls import path
from contacto.views import contact

from django.conf import settings

urlpatterns = [
    path('', contact, name="contacto"),
]

