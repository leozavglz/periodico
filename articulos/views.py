# articulos/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Articulo


class VistaListaArticulos(ListView):
    model = Articulo
    template_name = "articulos/lista.html"


class VistaDetalleArticulo(DetailView):
    model = Articulo
    template_name = "articulos/detalle.html"


class VistaCrearArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ["titulo", "cuerpo"]
    template_name = "articulos/nuevo.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class VistaEditarArticulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    fields = ["titulo", "cuerpo"]
    template_name = "articulos/editar.html"

    def test_func(self):
        articulo = self.get_object()
        return articulo.autor == self.request.user or self.request.user.is_staff


class VistaEliminarArticulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = "articulos/eliminar.html"
    success_url = reverse_lazy("articulo_lista")

    def test_func(self):
        articulo = self.get_object()
        return articulo.autor == self.request.user or self.request.user.is_staff


class VistaMisArticulos(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = "articulos/mios.html"

    def get_queryset(self):
        return Articulo.objects.filter(autor=self.request.user)
