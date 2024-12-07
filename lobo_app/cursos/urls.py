from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path(
        "curso_comprado/<int:curso_id>/",
        views.curso_comprado,
        name="curso_comprado",
    ),
]
