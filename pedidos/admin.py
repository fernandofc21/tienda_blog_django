from django.contrib import admin
from .models import Pedido, Producto, LineaPedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display=( "user", "created_at" )
    readonly_fields=('created_at', 'user')

class LineaPedidoAdmin(admin.ModelAdmin):
    list_display=( "user", "producto_id", "pedido_id", "created_at")
    readonly_fields=('created_at', 'cantidad')

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)