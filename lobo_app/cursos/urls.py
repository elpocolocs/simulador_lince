from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path(
        "curso_comprado/<int:curso_id>/",
        views.curso_comprado,
        name="curso_comprado",
    ),
    path(
        "vista_cursos/",
        views.listar_cursos_usuario,
        name="lista_cursos_usuario",
    ),
]
