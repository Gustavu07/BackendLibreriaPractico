from rest_framework import serializers
from Libreria.models import Compra, DetalleCompra
from Libreria.apis.detalle_compra_serializer import DetalleCompraSerializer

class CompraSerializer(serializers.ModelSerializer):
    detalles = DetalleCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ['id', 'usuario', 'fecha_compra', 'total', 'detalles']
        read_only_fields = ['usuario', 'fecha_compra', 'total']
