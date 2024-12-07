import random
import string

from cursos.models import Curso, CursosComprados
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


# Create your views here.
@login_required
def curso_comprado(request, curso_id):
    curso = get_object_or_404(
        Curso,
        id=curso_id,
    )

    try:
        curso_adquirido = CursosComprados.objects.get(
            usuario=request.user,
            curso_comprado=curso,
        )
    except:
        curso_adquirido = None

    print(type(curso_adquirido))
    mensaje = ""
    # Comprobamos si el usuario ya compró el curso
    if curso_adquirido:
        # El usuario ya compró el curso
        mensaje = "Ya compraste el curso"
    else:
        mensaje = "Compra exitosa"
        # El usuario no ha comprado el curso
        curso_adquirido = CursosComprados(usuario=request.user, curso_comprado=curso)
        codigo_compra = generar_contrasena()
        print(codigo_compra)
        curso_adquirido.codigo_compra = codigo_compra
        curso_adquirido.save()
    return render(
        request,
        "compra_exitosa.html",
        {
            "curso": curso,
            "mensaje": mensaje,
            "curso_adquirido": curso_adquirido,
        },
    )


def generar_contrasena(longitud=20):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
