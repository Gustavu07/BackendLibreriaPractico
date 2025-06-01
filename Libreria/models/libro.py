from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    isbn = models.CharField(max_length=20)
    #imagen = models.ImageField(upload_to='libros/', null=True, blank=True)

    generos = models.ManyToManyField('Genero', related_name='libros')
