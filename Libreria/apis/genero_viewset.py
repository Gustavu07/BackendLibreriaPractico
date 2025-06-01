from rest_framework import viewsets, status
from Libreria.models import Genero
from Libreria.apis.genero_serializer import GeneroSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Solo los administradores pueden crear géneros.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Solo los administradores pueden modificar géneros.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Solo los administradores pueden eliminar géneros.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
