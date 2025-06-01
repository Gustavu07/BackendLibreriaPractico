from rest_framework import serializers
from Libreria.models import Genero, Libro

class GeneroSerializer(serializers.ModelSerializer):
    libros = serializers.SerializerMethodField()

    class Meta:
        model = Genero
        fields = ['id', 'nombre', 'libros']

    def get_libros(self, obj):
        return [
            {
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor,
                'precio': libro.precio,
                'isbn': libro.isbn,
            }
            for libro in obj.libros.all()
        ]


class GeneroSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre']
