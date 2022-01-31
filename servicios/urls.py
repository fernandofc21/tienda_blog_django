from django.urls import path
from servicios.views import services



urlpatterns = [
    path('', services, name="servicios"),
]
