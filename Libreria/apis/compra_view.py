from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Libreria.models import Compra, Carrito, DetalleCompra
from Libreria.apis.compra_serializer import CompraSerializer
from django.db import transaction
class CompraViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Compra.objects.filter(usuario=self.request.user)

    @action(detail=False, methods=['post'])
    def comprar(self, request):
        user = request.user
        carrito_items = Carrito.objects.filter(usuario=user)

        if not carrito_items.exists():
            return Response({'error': 'El carrito está vacío.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            compra = Compra.objects.create(usuario=user, total=0)
            total = 0

            for item in carrito_items:
                precio = item.libro.precio
                DetalleCompra.objects.create(
                    compra=compra,
                    libro=item.libro,
                    precio_unitario=precio
                )
                total += precio

            compra.total = total
            compra.save()
            carrito_items.delete()

        return Response({'mensaje': 'Compra realizada con éxito', 'compra_id': compra.id, 'total': compra.total},
                        status=status.HTTP_201_CREATED)

