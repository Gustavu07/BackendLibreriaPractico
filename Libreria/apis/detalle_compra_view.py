from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Libreria.models import DetalleCompra
from Libreria.apis.detalle_compra_serializer import DetalleCompraSerializer

class DetalleCompraViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DetalleCompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Administrador').exists():
            return DetalleCompra.objects.all()
        return DetalleCompra.objects.filter(compra__usuario=user)
