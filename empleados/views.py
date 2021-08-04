from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Empleados

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 2
    model = Empleados


class ListarPorAreas(ListView):
    template_name = 'empleados/lista_contabilidad.html'
    
    # una forma de hacerlo
    # model = Empleados
    # queryset = Empleados.objects.filter(departamento__nombre='Ventas')
    
    # otra forma
    # def get_queryset(self):
    #     lista = Empleados.objects.filter(departamento__nombre='Ventas')
    #     return lista
    
    # obteniendo variable de la url
    def get_queryset(self):
        area = self.kwargs['shorname']
        print(area)
        lista = Empleados.objects.filter(departamento__nombreCorto=area)
        return lista


class listaEmpleadosPorFormulario(ListView):
    template_name = 'empleados/lista_por_formulario.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('Dentro de get_queryset')
        palabra_clave = self.request.GET.get('kword', '')
        print(palabra_clave)
        lista = Empleados.objects.filter(
            nombre=palabra_clave)
        print(lista)
        return lista


class habilidadesPorEmpleado(ListView):
    template_name = 'empleados/habilidades_por_empleados.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        empleado = Empleados.objects.get(id=8)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleados
    template_name = "empleados/empleado_detalle.html"
    context_object_name = 'empleado'


class Correcto(TemplateView):
    template_name = "empleados/correcto.html"


class CrearEmpleado(CreateView):
    model = Empleados
    template_name = "empleados/anadir_empleado.html"
    fields = ('__all__')
    success_url = reverse_lazy('empleados_app:web_correcta')


class EmpleadoUpdateView(UpdateView):
    model = Empleados
    template_name = "empleados/actualizar_empleado.html"
    fields = ('__all__')
    success_url = reverse_lazy('empleados_app:web_correcta')


class EmpleadoEliminar(DeleteView):
    model = Empleados
    template_name = "empleados/eliminar_empleado.html"
    success_url = reverse_lazy('empleados_app:web_correcta')
