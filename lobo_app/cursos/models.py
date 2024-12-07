from django.conf import settings
from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    photo = models.ImageField(
        upload_to="users/%Y/%m/%d/",
        blank=True,
    )
    precio = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.nombre}"


class CursosComprados(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cursos_comprados",  # Agregando un campo a la tabla usuarios llamado cursos_comprados
    )
    codigo_compra = models.CharField(max_length=20)  # Eso es para los códigos de compra
    curso_comprado = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="usuarios_inscritos",  # se crea en la tabla a la cual hace referencia, en este caso va a aparecer en la tabla de curso
    )
    fecha_compra = models.DateTimeField(
        auto_now=True
    )  # Cada que se crea un registro, se crea la fecha

    class Meta:
        indexes = [models.Index(fields=["-curso_comprado", "-usuario"])]
