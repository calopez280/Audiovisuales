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
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Equipo(models.Model):
    id_equipo = models.CharField(max_length=12)
    nombre_equipo = models.CharField(max_length=50)
    id_categoria= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    

    def __str__ (self):
        return "{0}-{1} ({2})".format(self.nombre_equipo, self.id_equipo, self.id_categoria)

class Facultad(models.Model):
    id_facultad = models.PositiveIntegerField
    nombre_facultad = models.CharField(max_length=50)

    def __str__ (self):
        return "{0}".format(self.nombre_facultad)

class Espacio(models.Model):
    id_espacio = models.PositiveIntegerField
    nombre_espacio = models.CharField(max_length=50)
    id_facultad= models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__ (self):
        return "{0} ({1})".format(self.nombre_espacio, self.id_facultad)

class facultad_equipo(models.Model):
    id_facultad= models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)
    id_equipo= models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
    id_facultad_equipo = models.PositiveIntegerField
    fecha_ingresado = models.DateField("Fecha De Creacion", auto_now= True, auto_now_add=False)

    def __str__(self):
        return "{0} - {1}".format(self.id_facultad, self.id_equipo)

class Estado(models.Model):
    id_estado = models.PositiveIntegerField
    nombre_estado = models.CharField(max_length=50)

    def __str__ (self):
        return "{0}".format(self.nombre_estado)

class Reserva(models.Model):
    id_reserva = models.PositiveIntegerField
    id_espacio= models.ForeignKey(Espacio, null=False, blank=False, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, null=False, blank=False, on_delete=models.CASCADE)
    id_equipo= models.ForeignKey(facultad_equipo, null=False, blank=False, on_delete=models.CASCADE)
    detalle_reserva = models.CharField(max_length=400)
    fecha_ingresado = models.DateField("Fecha De Creacion", auto_now= True, auto_now_add=False)

    def __str__ (self):
        return "{0}".format(self.detalle_reserva)

class Comentarios(models.Model):
    id_comentario = models.PositiveIntegerField
    detalle_reserva = models.CharField(max_length=400)

