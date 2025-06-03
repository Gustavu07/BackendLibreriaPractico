from django.db import models
from django.contrib.auth.models import User

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    #comprobante = models.FileField(upload_to='comprobantes/', null=True, blank=True)

    def __str__(self):
        return f'Compra #{self.id} de {self.usuario.username}'
