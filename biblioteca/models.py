from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    anio_publicacion = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

class Resena(models.Model):
    libro = models.ForeignKey(Libro, related_name='resenas', on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.PositiveIntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.libro.titulo}"

