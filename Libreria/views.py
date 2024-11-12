from django.shortcuts import render
from django.http import HttpResponse
from Libreria.models import Categorias
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



def Productos(request):
    return render(request,'Productos/Productos.html' )

def CrearProducto(request):
    return render(request,'Productos/CrearProducto.html' )

def EditarProducto(request):
    return render(request,'Productos/EditarProducto.html' )



def Clientes(request):
    return render(request,'Clientes/Clientes.html' )

def CrearCliente(request):
    return render(request,'Clientes/CrearCliente.html' )

def EditarCliente(request):
    return render(request,'Clientes/EditarCliente.html' )



def Empleados(request):
    return render(request,'Empleados/Empleados.html' )

def CrearEmpleado(request):
    return render(request,'Empleados/CrearEmpleado.html' )

def EditarEmpleado(request):
    return render(request,'Empleados/EditarEmpleado.html' )



def FacturaPagos(request):
    return render(request,'FacturaPagos/FacturaPagos.html' )

def CrearPago(request):
    return render(request,'FacturaPagos/CrearPago.html' )

def EditarPago(request):
    return render(request,'FacturaPagos/EditarPago.html' )



def MetodoPago(request):
    return render(request,'MetodoPago/MetodoPago.html' )

def AñadirMetodoPago(request):
    return render(request,'MetodoPago/AñadirMetodoPago.html' )

def EditarMetodoPago(request):
    return render(request,'MetodoPago/EditarMetodoPago.html' )