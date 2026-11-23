# cuentas/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioPersonalizado(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
