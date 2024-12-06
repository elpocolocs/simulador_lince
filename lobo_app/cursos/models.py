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
