from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = ""

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("register/", views.register, name="register"),
    path(
        "password-reset/",  # url
        auth_views.PasswordResetView.as_view(),  # Usa la vista genérica
        name="password_reset",  # nombre de la función pero en mi template
    ),
    path(
        "password-reset/done/",  # url
        auth_views.PasswordResetDoneView.as_view(),  # Usa la vista genérica
        name="password_reset_done",  # nombre de la función pero en mi template
    ),
    path(
        "password-reset/<uidb64>/<token>/",  # url
        auth_views.PasswordResetConfirmView.as_view(),  # Usa la vista genérica
        name="password_reset_confirm",  # nombre de la función pero en mi template
    ),
    path(
        "password-reset/complete/",  # url
        auth_views.PasswordResetCompleteView.as_view(),  # Usa la vista genérica
        name="password_reset_complete",  # nombre de la función pero en mi template
    ),
]
