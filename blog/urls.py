from django.urls import path
from blog.views import blog, categoria



urlpatterns = [
    path('', blog, name="blog"),
    path('categoria/<categoria_id>/', categoria, name="categoria")
]
