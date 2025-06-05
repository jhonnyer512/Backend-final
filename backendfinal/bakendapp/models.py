from django.db import models

# Modelo para representar productos o servicios
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# Modelo para testimonios de clientes
class Testimonio(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    comentario = models.TextField()
    foto = models.ImageField(upload_to='testimonios/', blank=True, null=True)

    def __str__(self):
        return self.nombre_cliente

# Modelo para mensajes de contacto
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