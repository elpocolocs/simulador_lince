from accounts.views import dashboard
from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    # path(
    #     "",
    #     views.listar_cursos_usuario,
    #     name="lista_cursos_usuario",
    # ),
    # path("<slug:category_slug>", dashboard, name="dasho"),
    # path("<int:id>/<slug:slug>/", views.curso_detail, name="curso_detail"),
    # path("curso_comprado/<int:curso_id>/", views.curso_comprado, name="curso_comprado"),
    path(
        "<slug:category_slug>",
        views.cursos_list,
        name="cursos_list_by_category",
    ),
    path("", views.cursos_list, name="cursos_list"),
]
