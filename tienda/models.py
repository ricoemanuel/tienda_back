from django.db import models

class Tienda(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_ventas= models.DecimalField(max_digits=20, decimal_places=10)

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    sku=models.CharField(max_length=255)
    nombre=models.CharField(max_length=255)
    descripcion=models.CharField(max_length=1000)
    unidades_disponibles=models.IntegerField(null=True, blank=True)
    precio_unitario=models.DecimalField(max_digits=20, decimal_places=10)
    tienda=models.ForeignKey(Tienda, on_delete=models.CASCADE)

class Usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)

class Carrito(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Items(models.Model):
    cantidad=models.IntegerField(null=True, blank=True)
    precio_venta=models.DecimalField(max_digits=20, decimal_places=10)
    descuento=models.DecimalField(max_digits=20, decimal_places=10)
    carrito=models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)