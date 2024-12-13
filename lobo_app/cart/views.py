from cursos.models import Curso
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddCourseForm


# Create your views here.
@require_POST
def cart_add(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Curso, id=course_id)
    form = CartAddCourseForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            curso=course,
            quantity=cd["quantity"],
            override_quantity=cd["override"],
        )
    return redirect("cart:cart_detail")


@require_POST
def cart_remove(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Curso, id=course_id)
    cart.remove(course)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddCourseForm(
            initial={"quantity": item["quantity"], "override": True},
        )
    return render(request, "detail.html", {"cart": cart})
