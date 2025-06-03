from django.db import models
from Libreria.models import Libro
from .compra import Compra

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.libro.titulo} - Compra #{self.compra.id}'
