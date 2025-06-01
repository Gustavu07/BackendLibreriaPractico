from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Libreria.models import Carrito
from Libreria.apis.carrito_serializer import CarritoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
