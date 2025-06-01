
from .carrito_view import CarritoViewSet
from .compra_view import CompraViewSet
from .detalle_compra_view import DetalleCompraViewSet
from .genero_viewset import GeneroViewSet
from .libros_viewset import LibroViewSet

from .carrito_serializer import CarritoSerializer
from .compra_serializer import CompraSerializer
from .detalle_compra_serializer import DetalleCompraSerializer
from .genero_serializer import GeneroSerializer, GeneroSimpleSerializer
from .libro_serializer import LibroSerializer



from .user_viewset import UserSerializer, UserViewSet, AuthViewSet