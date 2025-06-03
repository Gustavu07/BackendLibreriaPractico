from rest_framework import serializers
from Libreria.models import Carrito, Libro

class CarritoSerializer(serializers.ModelSerializer):
    libro_titulo = serializers.CharField(source='libro.titulo', read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'libro', 'libro_titulo', 'fecha_agregado']

    def validate_libro(self, value):
        user = self.context['request'].user
        if Carrito.objects.filter(usuario=user, libro=value).exists():
            raise serializers.ValidationError("Este libro ya está en el carrito.")
        return value
