from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.PositiveIntegerField
    nombre = models.CharField(max_length=50)

    def __str__ (self):
        return "{0} ({1})".format(self.nombre, self.id_rol)

class Usuario(models.Model):
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    id_rol= models.ForeignKey(Rol, null=False, blank=False, on_delete=models.CASCADE)

    def __str__ (self):
        return "({0}) {1}".format(self.cedula, self.nombre)
    
class Categoria(models.Model):
    id_categoria = models.PositiveIntegerField
    nombre = models.CharField(max_length=50)

    def __str__ (self):
        return "{0} ({1})".format(self.nombre, self.id_categoria)

class Equipo(models.Model):
    id_equipo = models.CharField(max_length=12)
    nombre_equipo = models.CharField(max_length=50)
    id_categoria= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)

    def __str__ (self):
        return "{0}-{1} ({2})".format(self.nombre_equipo, self.id_equipo, self.id_categoria)

class Facultad(models.Model):
    id_facultad = models.CharField(max_length=12)
    nombre_facultad = models.CharField(max_length=50)

    def __str__ (self):
        return "{0}-{1}".format(self.nombre_facultad, self.id_facultad)

class Espacio(models.Model):
    id_espacio = models.CharField(max_length=12)
    nombre_espacio = models.CharField(max_length=50)
    id_facultad= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)

    def __str__ (self):
        return "{0}-{1} ({2})".format(self.id_espacio, self.nombre_espacio, self.id_facultad)

class facultad_equipo(models.Model):
    id_facultad= models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)
    id_equipo= models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
    id_facultad_equipo = models.PositiveIntegerField

    def __str__(self):
        return "{0} - {1} ({2})".format(self.id_facultad, self.id_equipo, self.id_facultad_equipo)