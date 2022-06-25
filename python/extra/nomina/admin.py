from django.contrib import admin

# Register your models here.

from .models import Empresa, Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'sueldo', 'fecha_nac', 'empresa')
    #list_editable = ['fecha_nac','empresa']
    search_fields = ['nombre', 'apellido']

admin.site.register(Empleado, EmpleadoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'nit', 'tel', 'dir']
    list_display = ('id', 'nit', 'nombre', 'tel', 'dir')
    search_fields = ['nombre', 'nit']
    list_filter = ['dir']
    list_editable = ['tel']

admin.site.register(Empresa, EmpresaAdmin)


#Enviar DB del proyecto formativo.

#jor@misena.edu.co

