from rest_framework import serializers
from Libreria.models import Carrito, Libro

class CarritoSerializer(serializers.ModelSerializer):
    libro = serializers.PrimaryKeyRelatedField(queryset=Libro.objects.all())
    libro_titulo = serializers.SerializerMethodField()

    class Meta:
        model = Carrito
        fields = ['id', 'libro', 'libro_titulo', 'fecha_agregado']

    def get_libro_titulo(self, obj):
        return obj.libro.titulo

    def validate(self, attrs):
        user = self.context['request'].user
        libro = attrs.get('libro')

        if Carrito.objects.filter(usuario=user, libro=libro).exists():
            raise serializers.ValidationError("Este libro ya está en el carrito.")

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        return Carrito.objects.create(usuario=user, **validated_data)
