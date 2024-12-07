from cursos.models import Curso, CursosComprados
from django.shortcuts import get_object_or_404, render


# Create your views here.
def curso_comprado(request, curso_id):
    curso = get_object_or_404(
        Curso,
        id=curso_id,
    )
    curso_c = CursosComprados(usuario=request.user, curso_comprado=curso)
    curso_c.save()
    return render(request, "compra_exitosa.html", {"curso": curso})
