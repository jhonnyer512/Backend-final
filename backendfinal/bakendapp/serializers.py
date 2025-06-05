from rest_framework import serializers
from .models import Producto, Testimonio, MensajeContacto, Usuario

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TestimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonio
        fields = '__all__'

class MensajeContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeContacto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'