from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse(
            "cursos:cursos_list_by_category",
            args=[self.slug],
        )

    def __str__(self):
        return self.name


class Curso(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="cursos",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    photo = models.ImageField(
        upload_to="users/%Y/%m/%d/",
        blank=True,
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=now())
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["nombre"]),
            models.Index(fields=["-created"]),
        ]

    def get_absolute_url(self):
        return reverse(
            "cursos:curso_detail",
            args=[self.id, self.slug],
        )

    def __str__(self):
        return f"{self.nombre}"

    def save(self, *args, **kwargs):
        if not self.slug or self.nombre != Curso.objects.get(pk=self.pk).nombre:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


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
