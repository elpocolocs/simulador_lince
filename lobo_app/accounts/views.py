from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("account:dashboard")

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
