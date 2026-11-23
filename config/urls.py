# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cuentas/", include("django.contrib.auth.urls")),
    path("cuentas/", include("cuentas.urls")),
    path("articulos/", include("articulos.urls")),  # nuevo
    path("", include("paginas.urls")),
]
