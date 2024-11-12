from django.db import models

# Create your models here.
class Empleados(models.Model):
    Nombre = models.CharField(max_length=50)
    Usuario = models.TextField()
    Rol = models.TextField()

    def __str__(self):
        return self.Nombre


class Categorias(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()

    def __str__(self):
        return self.Nombre

class Productos(models.Model):
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Empleados = models.ForeignKey(Empleados, on_delete=models.PROTECT)
    Categorias = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    Imagen = models.ImageField(upload_to="Producto", null=True)

    def __str__(self):
        return self.Nombre

class MetodoPago(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre


class Clientes(models.Model):
    Nombre = models.CharField(max_length=50)
    Correo = models.TextField()
    Identificacion = models.IntegerField()

    def __str__(self):
        return self.Nombre

class FacturaPagos(models.Model):
    Fecha = models.DateField()
    CantidadProductos = models.IntegerField()
    Valor = models.IntegerField()
    Productos = models.ForeignKey(Productos, on_delete=models.PROTECT)
    MetodoPago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    Clientes = models.ForeignKey(Clientes, on_delete=models.PROTECT)

    def __str__(self):
        return f"Factura {self.id} - {self.Fecha}"



