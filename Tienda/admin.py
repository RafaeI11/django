from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'imagen')
    list_filter = ('categorias',)
    search_fields = ('nombre', 'categorias__nombre')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_pedido', 'total', 'estimacion_entrega')
    list_filter = ('cliente',)
    search_fields = ('cliente__username',)

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)
