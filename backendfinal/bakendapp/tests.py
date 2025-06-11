from django.test import TestCase, Client
from .models import Usuario, PerfilActivo, Producto, Bebida, Carrito, MensajeContacto

class UsuarioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario_data = {
            "nombre": "Juan",
            "correo": "juan@example.com",
            "contrasena": "1234"
        }
        self.crear_usuario_url = '/api/crear-usuario/'
        self.login_url = '/api/login/'

    def test_crear_usuario(self):
        response = self.client.post(
            self.crear_usuario_url,
            data=self.usuario_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Usuario.objects.count(), 1)

    def test_login_usuario_correcto(self):
        self.client.post(
            self.crear_usuario_url,
            data=self.usuario_data,
            content_type='application/json'
        )

        login_data = {
            "correo": "juan@example.com",
            "contrasena": "1234"
        }

        response = self.client.post(
            self.login_url,
            data=login_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

    def test_login_usuario_incorrecto(self):
        login_data = {
            "correo": "noexiste@example.com",
            "contrasena": "incorrecta"
        }

        response = self.client.post(
            self.login_url,
            data=login_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("mensaje", response.json())


from bakendapp.models import PerfilActivo

def test_crear_perfil_activo(self):
    perfil = PerfilActivo.objects.create(
        nombre="Activo1",
        correo="activo@example.com",
        contrasena="pass"
    )
    self.assertEqual(perfil.nombre, "Activo1")



class ProductoTests(TestCase):
    def test_crear_producto(self):
        producto = Producto.objects.create(
            nombre="Producto1",
            descripcion="Descripción de producto",
            imagen="productos/test.jpg",
            precio=10.99
        )
        self.assertEqual(producto.precio, 10.99)
        self.assertIn("Producto1", str(producto))


class BebidaTests(TestCase):
    def test_crear_bebida(self):
        bebida = Bebida.objects.create(
            nombre="Coca-Cola",
            descripcion="Bebida gaseosa",
            imagen="Bebidas/coca.jpg",
            precio=8.50
        )
        self.assertEqual(bebida.nombre, "Coca-Cola")
        self.assertGreater(bebida.precio, 0)


class CarritoTests(TestCase):
    from bakendapp.models import Producto, Carrito  # asegúrate de importar ambos
    def test_crear_carrito(self):
        producto = Producto.objects.create(nombre="Producto1", precio=10.0)  # ajusta los campos según tu modelo
        carrito = Carrito.objects.create(
            producto=producto,  # ✅ esta es la corrección
            bebida="Coca-Cola",
            cantidad=2
        )
        self.assertEqual(carrito.cantidad, 2)



class MensajeContactoTests(TestCase):
    def test_crear_mensaje_contacto(self):
        mensaje = MensajeContacto.objects.create(
            nombre="Cliente",
            email="cliente@example.com",
            mensaje="Quiero más información."
        )
        self.assertEqual(mensaje.email, "cliente@example.com")
        self.assertIn("información", mensaje.mensaje)