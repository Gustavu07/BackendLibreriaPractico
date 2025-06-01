from rest_framework import serializers
from Libreria.models import DetalleCompra

class DetalleCompraSerializer(serializers.ModelSerializer):
    libro_titulo = serializers.CharField(source='libro.titulo', read_only=True)

    class Meta:
        model = DetalleCompra
        fields = ['id', 'libro', 'libro_titulo', 'precio_unitario']
