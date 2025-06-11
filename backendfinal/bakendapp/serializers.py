from rest_framework import serializers
from .models import Producto, PerfilActivo, MensajeContacto, Usuario, Bebida, Carrito

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = '__all__'

class MensajeContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeContacto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PerfilActivoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()  

    class Meta:
        model = PerfilActivo
        fields = '__all__'

    

class CarritoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    bebida = BebidaSerializer(read_only=True)

    producto_id = serializers.PrimaryKeyRelatedField(
        source='producto', queryset=Producto.objects.all(), write_only=True, required=False
    )
    bebida_id = serializers.PrimaryKeyRelatedField(
        source='bebida', queryset=Bebida.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Carrito
        fields = ['id', 'producto', 'producto_id', 'bebida', 'bebida_id', 'cantidad']
