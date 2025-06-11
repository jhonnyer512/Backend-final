from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Producto, Bebida, MensajeContacto, Usuario, PerfilActivo, Carrito
from .serializers import (
    ProductoSerializer, BebidaSerializer, MensajeContactoSerializer,
    UsuarioSerializer, PerfilActivoSerializer, CarritoSerializer
)

# --- ViewSets para modelos estándar ---
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer

class MensajeContactoViewSet(viewsets.ModelViewSet):
    queryset = MensajeContacto.objects.all()
    serializer_class = MensajeContactoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilActivoViewSet(viewsets.ModelViewSet):
    queryset = PerfilActivo.objects.all()
    serializer_class = PerfilActivoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

# --- Vistas personalizadas ---
@api_view(['GET'])
def bebida_list(request):
    bebidas = Bebida.objects.all()
    serializer = BebidaSerializer(bebidas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def usuario_list(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_usuario(request):
    correo = request.data.get('correo')
    contrasena = request.data.get('contrasena')

    if not correo or not contrasena:
        return Response({"mensaje": "Correo y contraseña requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
        return Response({
            "mensaje": "Login exitoso",
            "token": "token_simulado",  # Aquí deberías integrar JWT o algún sistema real
            "nombre": usuario.nombre
        }, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({"mensaje": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
