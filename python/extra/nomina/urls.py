from django.urls import path

from . import views

app_name = 'nomina'
urlpatterns = [
    path('', views.index, name='index'),
    path('acercade/', views.acercaDe, name='acercade'),
    path('saludo/<str:nombre>/', views.saludar, name='saludo'),

    path('empresas/', views.empresas, name='empresas'),
    path('eliminar_empresa/<int:id>', views.eliminarEmpresas, name='eliminar_empresa'),
    path('formulario_empresa/', views.formularioEmpresas, name='formulario_empresa'),
    path('guardar_empresa/', views.guardarEmpresa, name='guardar_empresa'),
    path('eliminar_empresa/<int:id>', views.eliminarEmpresas, name='eliminar_empresa'),
    path('formulario_empresa_editar/<int:id>', views.formularioEmpresasEditar, name='formulario_empresa_editar'),
    path('actualizar_empresa/', views.actualizarEmpresa , name="actualizar_empresa"),
    path('buscar_empresas/', views.buscar, name='buscar_empresas'),


    path('empleados/', views.empleados, name='empleados'),
    
]

