from django.db import models
from django.contrib.auth.models import User
from Libreria.models import Libro

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrito')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('usuario', 'libro')
