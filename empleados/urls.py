from django.contrib import admin
from django.urls import path
from . import views


#def desdedepartamento(self):
#    print('Desde urls de departamento')

app_name = 'empleados_app'
urlpatterns = [
    path('listar_todos_empleados/', views.ListAllEmpleados.as_view()),
    path('listar_departamento/<shorname>', views.ListarPorAreas.as_view()),
    path('buscar_empleado', views.listaEmpleadosPorFormulario.as_view()),
    path('list_all', views.ListAllEmpleados.as_view()),
    path('habilidades_por_empleados', views.habilidadesPorEmpleado.as_view()),
    path('empleado_detalle/<pk>', views.EmpleadoDetailView.as_view()),
    path('anadir_empleado', views.CrearEmpleado.as_view()),
    path(
        'correcto', 
        views.Correcto.as_view(), 
        name='web_correcta'),
    path('actualizar_empleado/<pk>', 
         views.EmpleadoUpdateView.as_view(),
         name='actualizar'),
    path('eliminar_empleado/<pk>',
         views.EmpleadoEliminar.as_view(),
         name='eliminar'),
]
