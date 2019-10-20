from django.contrib import admin
from .models import Categoria, Equipo,Facultad, Espacio, facultad_equipo, Estado, Reserva

admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Facultad)
admin.site.register(Espacio)
admin.site.register(facultad_equipo)
admin.site.register(Estado)
admin.site.register(Reserva)