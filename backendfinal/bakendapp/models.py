from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='bebidas/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class PerfilActivo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.nombre

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto or self.bebida} x {self.cantidad}"

def test_crear_carrito(self):
    producto = Producto.objects.create(nombre="Producto1", precio=10.0)  # ajusta campos reales
    carrito = Carrito.objects.create(
        producto=producto,  # aquí va la instancia, no un string
        bebida="Coca-Cola",
        cantidad=2
    )
    self.assertEqual(carrito.cantidad, 2)