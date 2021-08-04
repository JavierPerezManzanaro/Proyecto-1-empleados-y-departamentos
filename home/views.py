from django.shortcuts import render


from django.views.generic import TemplateView, ListView, CreateView

from .models import Pruebabbdd

from .forms import PruebaFormulario

class Prueba(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/list.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']

class ListaPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Pruebabbdd
    context_object_name = 'registros'
    #queryset = all


class CrearRegistro(CreateView):
    template_name = 'home/crear.html'
    model = Pruebabbdd
    form_class = PruebaFormulario
    success_url = '/'
