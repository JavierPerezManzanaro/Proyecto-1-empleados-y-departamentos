from django.contrib import admin
from django.urls import path

from . import views
#def desdedepartamento(self):
#    print('Desde urls de departamento')

urlpatterns = [
    path('new_departamento/', views.NuevoDepartamento.as_view(), name = 'nuevo_departamento'),
]
