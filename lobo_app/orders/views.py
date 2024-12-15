import random
import string
from datetime import datetime

from cart.cart import Cart
from cart.forms import CartAddCourseForm
from cursos.models import Category, Curso, CursosComprados
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render

from .forms import OrderCreateForm
from .models import OrderItem


def generar_contrasena(longitud=20):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            clave = generar_contrasena()
            order = form.save()
            order.key = clave
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    course=item["curso"],
                    price=item["price"],
                    quantity=item["quantity"],
                    user=request.user,
                )
            cuerpo_correo = f"""
            {request.user.username} gracias por su compra. 
            Su clave de compra es {clave}. 
            
            Lo esperamos pronto.
"""
            send_mail(
                "Cursos lince",
                cuerpo_correo,
                "pocoluc@gmail.com",
                [request.user.email],
            )
            # limpiar el carrito
            cart.clear()
            return render(
                request,
                "created.html",
                {
                    "order": order,
                },
            )
    else:
        form = OrderCreateForm()
    return render(
        request,
        "create.html",
        {
            "cart": cart,
            "form": form,
        },
    )


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


def list_user_courses(request):
    item_list = OrderItem.objects.filter(user=request.user)
    courses_list = []
    for item in item_list:
        cc = get_object_or_404(Curso, id=item.course.id)
        courses_list.append(cc)
    print(courses_list)

    return render(
        request,
        "listing_courses.html",
        {"lista_cursos": courses_list, "hero_message": "Estos son tus cursos"},
    )
