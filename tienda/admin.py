from django.contrib import admin
from .models import CategoriaProducto, Producto
# Register your models here.


class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display=( "nombre", "created", "updated" )
    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    list_display=( "nombre", "precio", "disponibilidad", "created", "updated", "categoria", "imagen" )
    readonly_fields=('created', 'updated')

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)