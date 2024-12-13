from django.contrib import admin

from .models import Category, Curso


# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "descripcion",
        "photo",
        "precio",
        "slug",
        "available",
        "created",
        "updated",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["precio", "available"]
    prepopulated_fields = {
        "slug": ("nombre",),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {
        "slug": ("name",),
    }
