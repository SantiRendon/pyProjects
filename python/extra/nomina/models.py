from django.db import models

# Create your models here.
class Empresa(models.Model):
    nit = models.CharField(max_length=15, null=False)
    nombre = models.CharField(max_length=100, null=False, unique=True)
    tel = models.CharField(max_length=15, null=True)
    dir = models.CharField(max_length=254, null=False)

    def __str__(self):
        return str(self.id) + " - " + str(self.nombre)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    correo = models.EmailField(max_length=254, unique=True, null=False)
    sueldo = models.IntegerField(null=False)
    fecha_nac = models.DateField('YYYY-MM-DD')
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre + " " + self.apellido

