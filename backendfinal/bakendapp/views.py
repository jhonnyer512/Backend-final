from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto, Testimonio, MensajeContacto
from .serializers import ProductoSerializer, TestimonioSerializer, MensajeContactoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

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