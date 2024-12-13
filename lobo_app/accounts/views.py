from cursos.models import Category, Curso
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserRegistrationForm


# Create your views here.
def dashboard(request, category_slug=None):
    if not request.user.is_authenticated:
        return redirect("login")
    category = None
    categories = Category.objects.all()
    all_cursos = Curso.objects.all()  # Obtiene todos los cursos de la tabla curso
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        all_cursos = all_cursos.filter(category=category)
    return render(
        request,
        "dashboard.html",
        {
            "all_cursos": all_cursos,
            "categories": categories,
            "category": category,
        },
    )


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Crear nuevo usuario
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(
                request,
                "register_done.html",
                {"new_user": new_user},
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        "register.html",
        {"user_form": user_form},
    )
