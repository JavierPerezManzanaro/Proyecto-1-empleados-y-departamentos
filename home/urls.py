from django.contrib import admin
from django.urls import path
from . import views

#def desdedepartamento(self):
#    print('Desde urls de departamento')

urlpatterns = [
    path('home/prueba/', views.Prueba.as_view()),
    path('home/lista/', views.PruebaListView.as_view()),
    path('home/lista_prueba/', views.ListaPrueba.as_view()),
    path('home/crear/', views.CrearRegistro.as_view(), name = 'prueba'),
    
]
