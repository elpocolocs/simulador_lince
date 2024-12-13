import random
import string
from datetime import datetime

from cart.forms import CartAddCourseForm
from cursos.models import Category, Curso, CursosComprados
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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

    # print(type(curso_adquirido))
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
        fecha_legible = curso_adquirido.fecha_compra.strftime(
            "%A, %d de %B de %Y, %H:%M:%S"
        )
        cuerpo_correo = f"""Usuario {request.user.username}:

        Felicidades, ha comprado el curso {curso.nombre}, con fecha {fecha_legible}.

        Su código de acceso es: {curso_adquirido.codigo_compra}.
        """

        send_mail(
            "Cursos lince",
            cuerpo_correo,
            "pocoluc@gmail.com",
            [request.user.email],
        )
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


def listar_cursos_usuario(request):
    lista_cursos = CursosComprados.objects.filter(usuario=request.user)
    print(lista_cursos)
    return render(
        request,
        "lista_cursos.html",
        {"lista_cursos": lista_cursos, "hero_message": "Estos son mis cursos"},
    )


def curso_detail(request, id, slug):
    curso = get_object_or_404(
        Curso,
        id=id,
        slug=slug,
        available=True,
    )
    return render(
        request,
        "detail.html",
        {
            "curso": curso,
        },
    )


def cursos_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cursos = Curso.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(
            Category,
            slug=category_slug,
        )
        cursos = cursos.filter(category=category)
    cart_course_form = CartAddCourseForm()
    return render(
        request,
        "list_courses.html",
        {
            "category": category,
            "categories": categories,
            "cursos": cursos,
            "cart_course_form": cart_course_form,
        },
    )
