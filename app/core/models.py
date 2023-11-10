from django.db import models

# Create your models here.


class Empleado(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField( null=False, blank=False)
    numero_empleado = models.IntegerField( null=False, blank=False, unique=True)
    curp = models.CharField(max_length=18, null=False, blank=False, unique=True)
    ssn = models.CharField(max_length=20, null=False, blank=False, unique=True)
    numero_telefono = models.CharField(max_length=10, null=False, blank=False)
    nacionalidad = models.CharField(max_length=30, null=False, blank=False)


class Beneficiario(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField( null=False, blank=False)
    porcentaje = models.IntegerField( null=False, blank=False)
    curp = models.CharField(max_length=18, null=False, blank=False, unique=True)
    ssn = models.CharField(max_length=20, null=False, blank=False, unique=True)
    numero_telefono = models.CharField(max_length=10, null=False, blank=False)
    nacionalidad = models.CharField(max_length=30, null=False, blank=False)