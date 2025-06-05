from django.test import TestCase, Client
from .models import Usuario

class UsuarioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario_data = {
            "nombre": "Juan",
            "correo": "juan@example.com",
            "contrasena": "1234"
        }

    def test_crear_usuario(self):
        response = self.client.post(
            '/api/usuario/',
            data=self.usuario_data,
            content_type='application/json'  # <- Agrega esto
        )
        self.assertEqual(response.status_code, 201)

    def test_login_usuario_correcto(self):
        # Crear usuario primero
        self.client.post(
            '/api/usuario/',
            data=self.usuario_data,
            content_type='application/json'  # <- También aquí
        )

        login_data = {
            "correo": "juan@example.com",
            "contrasena": "1234"
        }

        response = self.client.post(
            '/api/login/',
            data=login_data,
            content_type='application/json'  # <- Y aquí
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())