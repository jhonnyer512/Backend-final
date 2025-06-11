from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductoViewSet, BebidaViewSet, MensajeContactoViewSet, UsuarioViewSet,
    PerfilActivoViewSet, CarritoViewSet,
    bebida_list, usuario_list, crear_usuario, login_usuario
)

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'bebidas', BebidaViewSet)
router.register(r'contactos', MensajeContactoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfiles-activos', PerfilActivoViewSet)
router.register(r'carrito', CarritoViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Endpoints adicionales (sin ViewSet)
    path('api/bebidas/', bebida_list, name='bebida-list'),
    path('api/usuarios/', usuario_list, name='usuario-list'),
    path('api/crear-usuario/', crear_usuario, name='crear-usuario'),
    path('api/login/', login_usuario, name='login'),
]
