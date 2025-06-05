from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto, Testimonio, MensajeContacto, Usuario
from .serializers import ProductoSerializer, TestimonioSerializer, MensajeContactoSerializer, UsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TestimonioViewSet(viewsets.ModelViewSet):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer

class MensajeContactoViewSet(viewsets.ModelViewSet):
    queryset = MensajeContacto.objects.all()
    serializer_class = MensajeContactoSerializer

class ProductoListView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class UsuarioListView(APIView):
    def get(self, request):
        usuarios = usuarios.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def crear_usuario(request):
    serializer = UsuarioSerializer(data=request.data if hasattr(request, 'data') else request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_usuario(request):
    data = request.data if hasattr(request, 'data') else request.POST

    correo = data.get('correo')
    contrasena = data.get('contrasena')

    if not correo or not contrasena:
        return Response({"mensaje": "Correo y contraseña requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
        return Response({"mensaje": "Login exitoso",
                        "token": "token_simulado",
                        "nombre": usuario.nombre}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({"mensaje": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
