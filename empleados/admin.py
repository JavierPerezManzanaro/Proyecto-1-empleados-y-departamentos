from django.contrib import admin

from .models import Empleados, Habilidades


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'puesto', 'Nombre_y_apellido',)
    search_fields = ('apellido',)
    list_filter = ('puesto', 'habilidades',)
    filter_horizontal = ('habilidades',)


    def Nombre_y_apellido(self, objet): 
        print(objet)  # se ve en la terminal
        return objet.nombre + ' ' + objet.apellido  # se ve en la web del admin
    
    
admin.site.register(Empleados, EmpleadoAdmin)
