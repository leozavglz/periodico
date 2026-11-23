# cuentas/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FormularioCambioUsuario, FormularioCreacionUsuario
from .models import UsuarioPersonalizado


@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = FormularioCreacionUsuario
    form = FormularioCambioUsuario
    list_display = ["username", "email", "edad", "ciudad", "is_staff"]
    search_fields = ["username", "email"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["edad", "ciudad"]}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "username",
                    "email",
                    "edad",
                    "ciudad",
                    "password1",
                    "password2",
                ],
            },
        ),
    )
