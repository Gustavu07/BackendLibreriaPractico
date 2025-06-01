from rest_framework import serializers
from Libreria.models import Libro, Genero
from Libreria.apis.genero_serializer import GeneroSimpleSerializer

class LibroSerializer(serializers.ModelSerializer):
    genero_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(),
        source='generos',
        many=True,
        write_only=True
    )
    generos = GeneroSimpleSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Libro
        fields = '__all__'
