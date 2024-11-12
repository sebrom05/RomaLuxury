from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),


    path('Catalogo', views.Catalogo, name='Catalogo'),


    path('Categorias', views.Categorias_1, name='Categorias'),
    path('Categorias/CrearCategoria', views.CrearCategoria, name='CrearCategoria'),
    path('Categorias/EditarCategoria/<int:id>', views.EditarCategoria, name='EditarCategoria'),
    path('Categorias/BorrarCategoria/<int:id>', views.BorrarCategoria, name='BorrarCategoria'),

    path('Productos', views.Productos, name='Productos'),
    path('Productos/CrearProducto', views.CrearProducto, name='CrearProducto'),
    path('Categorias/EditarProducto', views.EditarProducto, name='EditarProducto'),


    path('Clientes', views.Clientes, name='Clientes'),
    path('Clientes/CrearCliente', views.CrearCliente, name='CrearCliente'),
    path('Clientes/EditarCliente', views.EditarCliente, name='EditarCliente'),


    path('Empleados', views.Empleados, name='Empleados'),
    path('Empleados/CrearEmpleado', views.CrearEmpleado, name='CrearEmpleado'),
    path('Empleados/EditarEmpleado', views.EditarEmpleado, name='EditarEmpleado'),

    path('FacturaPagos', views.FacturaPagos, name='FacturaPagos'),
    path('FacturaPagos/CrearPago', views.CrearPago, name='CrearPago'),
    path('FacturaPagos/EditarPago', views.EditarPago, name='EditarPago'),

    path('MetodoPago', views.MetodoPago, name='MetodoPago'),
    path('MetodoPago/AñadirMetodoPago', views.AñadirMetodoPago, name='AñadirMetodoPago'),
    path('MetodoPago/EditarMetodoPago', views.EditarMetodoPago, name='EditarMetodoPago'),


]