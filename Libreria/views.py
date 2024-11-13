from django.shortcuts import render
from django.http import HttpResponse
from Libreria.models import Categorias, Clientes, Productos, Empleados, FacturaPagos, MetodoPago
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def inicio(request):
    return render(request, "pagina/inicio.html")

def nosotros(request):
    return render(request, 'pagina/nosotros.html')



def Catalogo(request):
    return render(request, 'Catalogo/Catalogo.html')


def Categorias_1(request):
    categorias = Categorias.objects.all()  # Obtiene todas las categorías
    return render(request, 'Categorias/Categorias.html', {'categorias': categorias})

def CrearCategoria(request):
    return render(request, 'Categorias/CrearCategoria.html')

def EditarCategoria(request, id):
    print(id, "Este es el id")
    return render(request, 'Categorias/EditarCategoria.html', {'id': id})

def BorrarCategoria(request,id):
    return render(request, 'Categorias/BorrarCategoria.html')



def Productos_1(request):
    productos = Productos.objects.all()
    return render(request,'Productos/Productos.html', {'productos': productos} )

def CrearProducto(request):
    return render(request,'Productos/CrearProducto.html' )

def EditarProducto(request,id):
    print(id, "Este es el id")
    return render(request,'Productos/EditarProducto.html', {'id': id} )

def EliminarProducto(request,id):
    return render(request, 'Productos/EliminarProducto.html')



def Clientes_1(request):
    clientes = Clientes.objects.all()  # Obtiene todas las categorías
    return render(request,'Clientes/Clientes.html', {'clientes': clientes} )

def CrearCliente(request):
    return render(request,'Clientes/CrearCliente.html' )

def EditarCliente(request,id):
    print(id, "Este es el id")
    return render(request,'Clientes/EditarCliente.html', {'id': id})

def BorrarCliente(request,id):
    return render(request, 'Clientes/BorrarCliente.html')



def Empleados_1(request):
    empleados = Empleados.objects.all()
    return render(request,'Empleados/Empleados.html', {'empleados': empleados} )

def CrearEmpleado(request):
    return render(request,'Empleados/CrearEmpleado.html' )

def EditarEmpleado(request,id):
    print(id, "Este es el id")
    return render(request,'Empleados/EditarEmpleado.html', {'id': id} )

def EliminarEmpleado(request,id):
    return render(request, 'Empleados/EliminarEmpleado.html')



def FacturaPagos_1(request):
    facturapagos = FacturaPagos.objects.all()
    return render(request,'FacturaPagos/FacturaPagos.html', {'facturapagos' : facturapagos} )

def CrearPago(request):
    return render(request,'FacturaPagos/CrearPago.html' )

def EditarPago(request,id):
    print(id, "Este es el id")
    return render(request,'FacturaPagos/EditarPago.html', {'id': id} )

def BorrarPago(request,id):
    return render(request,'FacturaPagos/BorrarPago.html' )


def MetodoPago_1(request):
    metodopagos =MetodoPago.objects.all()
    return render(request,'MetodoPago/MetodoPago.html', {'metodopagos' : metodopagos} )

def AñadirMetodoPago(request):
    return render(request,'MetodoPago/AñadirMetodoPago.html' )

def EditarMetodoPago(request,id):
    print(id, "Este es el id")
    return render(request,'MetodoPago/EditarMetodoPago.html', {'id': id} )

def BorrarMetodoPago(request):
    return render(request,'MetodoPago/BorrarMetodoPago.html' )