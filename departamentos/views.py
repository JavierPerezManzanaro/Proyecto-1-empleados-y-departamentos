from django.shortcuts import render

from django.views.generic.edit import FormView


from .forms import NuevoDepartamento

from empleados.models import Empleados
from .models import Departamento

class NuevoDepartamento(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NuevoDepartamento
    success_url = '/'
    
    def form_valid(self, form):
        print('estamos aquí')

        #datos del departamento
        nuevoDepartamento = Departamento(
            nombre = form.cleaned_data['departamento'],
            nombreCorto=form.cleaned_data['shortname']
        )
        nuevoDepartamento.save()

        #datos del usuario
        nombreFormulario = form.cleaned_data['nombre']
        apellidosFormulario = form.cleaned_data['apellidos']
        Empleados.objects.create(
            nombre=nombreFormulario,
            apellido=apellidosFormulario,
            departamento=nuevoDepartamento
            )
        return super(NuevoDepartamento, self).form_valid(form)
