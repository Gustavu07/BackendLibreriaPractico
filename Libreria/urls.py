from django.urls import path, include
from rest_framework import routers


from Libreria.apis import (LibroViewSet, GeneroViewSet, UserViewSet, AuthViewSet,
                           CarritoViewSet, CompraViewSet)
from Libreria.apis.detalle_compra_view import DetalleCompraViewSet

router = routers.DefaultRouter()

router.register('libros', LibroViewSet)
router.register('generos', GeneroViewSet)
router.register("usuarios", UserViewSet, basename='usuarios')
router.register("auth", AuthViewSet, basename='auth')
router.register('carrito', CarritoViewSet, basename='carrito')
router.register('compras', CompraViewSet, basename='compras')

router.register('detalle-compra', DetalleCompraViewSet, basename='detalle-compra')

urlpatterns = [
    path('', include(router.urls)),
]