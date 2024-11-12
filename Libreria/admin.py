from django.contrib import admin
from .models import Empleados, Categorias, Productos, MetodoPago , Clientes, FacturaPagos
# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
    list_display=['Nombre', 'Usuario', 'Rol']

class CategoriasAdmin(admin.ModelAdmin):
    list_display=['Nombre', 'Descripcion']

class ClientesAdmin(admin.ModelAdmin):
    list_display=['Nombre', 'Correo', 'Identificacion']

class FacturaPagosAdmin(admin.ModelAdmin):
    list_display=['Fecha', 'CantidadProductos', 'Valor','Productos', 'MetodoPago', 'Clientes']

class ProductosAdmin(admin.ModelAdmin):
    list_display=['Nombre', 'Precio', 'Empleados','Categorias', 'Imagen']

admin.site.register(Empleados,EmpleadosAdmin )
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(MetodoPago)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(FacturaPagos, FacturaPagosAdmin)