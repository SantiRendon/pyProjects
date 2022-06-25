from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Importamos los modelos del ORM (Bases de Datos)
from .models import Empresa, Empleado

def index(request):
    return render(request, 'nomina/index.html')

def empresas(request):
    q = Empresa.objects.all()
    
    paginator = Paginator(q, 3) #Mostrar 3 registros por página
    page_number = request.GET.get('page')
    q = paginator.get_page(page_number)

    contexto = {'data': q}    
    return render(request, 'nomina/empresas.html', contexto)

def eliminarEmpresas(request, id):
    #obtener objeto a través de ID
    q = Empresa.objects.get(pk = id)
    q.delete()
    contexto = { 'empresa': q.nombre }
    return render(request, 'nomina/empresa_confirm_delete.html', contexto)

def formularioEmpresas(request):
    return render(request, 'nomina/empresa_formulario.html')

def guardarEmpresa(request):
    q = Empresa(
        nit = request.POST["nit"],
        nombre = request.POST["nombre"],
        tel = request.POST["tel"],
        dir = request.POST["dir"]
    )
    q.save()
    return HttpResponseRedirect(reverse('nomina:empresas'))
    #  , args=(question.id,)

def formularioEmpresasEditar(request, id):
    q = Empresa.objects.get(pk = id)
    contexto = { 'data': q }
    return render(request, 'nomina/empresa_formulario_editar.html', contexto)

def actualizarEmpresa(request):
    #Consulto por <<id>> la empresa y obtengo un objeto....
    e = Empresa.objects.get(pk = request.POST["id"])

    #actualizo los atributos del objeto, por los que viene del form
    e.nit = request.POST["nit"]
    e.nombre = request.POST["nombre"]
    e.tel = request.POST["tel"]
    e.dir = request.POST["dir"]
    
    #actualizamos el objeto en BD.
    e.save()
    return HttpResponseRedirect(reverse('nomina:empresas'))

def buscar(request):
    q = Empresa.objects.filter(nombre__icontains = request.POST["dato"])
    contexto = {'data': q}
    return render(request, 'nomina/empresas.html', contexto)

def empleados(request):
    q = Empleado.objects.all()
    contexto = {'data': q}
    return render(request, 'nomina/empleados.html', contexto)


def acercaDe(request):
    return HttpResponse("Este software es desarrollado por JorGarcia<br><a href='../'>Volver</a>")

def saludar(request, nombre):
    return HttpResponse(f"Hola <strong style='color:red'>{nombre}<strong>")