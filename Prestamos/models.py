from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__ (self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Equipo(models.Model):
    id_equipo = models.CharField(max_length=12, primary_key=True)
    nombre_equipo = models.CharField(max_length=50)
    id_categoria= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    

    def __str__ (self):
        return "{0}-{1} ({2})".format(self.nombre_equipo, self.id_equipo, self.id_categoria)

class Facultad(models.Model):
    nombre_facultad = models.CharField(max_length=50)

    def __str__ (self):
        return "{0}".format(self.nombre_facultad)

class Espacio(models.Model):
    nombre_espacio = models.CharField(max_length=50)
    id_facultad= models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__ (self):
        return "{0} ({1})".format(self.nombre_espacio, self.id_facultad)

class facultad_equipo(models.Model):
    id_facultad= models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)
    id_equipo= models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
    fecha_ingresado = models.DateField("Fecha De Creacion", auto_now= True, auto_now_add=False)

    def __str__(self):
        return "{0} - {1}".format(self.id_facultad, self.id_equipo)


class Reserva(models.Model):
    id_espacio= models.ForeignKey(Espacio, null=False, blank=False, on_delete=models.CASCADE)
    id_equipo= models.ForeignKey(facultad_equipo, null=False, blank=False, on_delete=models.CASCADE)
    detalle_reserva = models.TextField()
    fecha_solicitud = models.DateTimeField("Fecha De Solicitud", auto_now_add=False)

    def __str__ (self):
        return "{0}".format(self.detalle_reserva)

class Comentarios(models.Model):
    
    id_reserva= models.ForeignKey(Reserva, null=False, blank=False, on_delete=models.CASCADE)
    detalle_reserva = models.TextField()
    
    LOAN_STATUS = (
        ('r', 'Reservado'),
        ('e', 'Entregado'),
        ('f', 'Finalizado'),
    )
    id_estado= models.CharField(max_length=1, choices=LOAN_STATUS, null=False, default='r')

    def __str__ (self):
        return "{0}".format(self.id_reserva)

class comentario_servicio(models.Model):
    detalle_servicio = models.TextField()
    
    LOAN_STATUS = (
        ('p', 'Pesimo'),
        ('m', 'Malo'),
        ('r', 'Regular'),
        ('b', 'Bueno'),
        ('e', 'Excelente'),
    )
    id_estado= models.CharField(max_length=1, choices=LOAN_STATUS, null=False)

    def __str__ (self):
        return "{0}".format(self.id_estado)
