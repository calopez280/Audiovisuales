from django.contrib import admin
from .models import Categoria, Equipo,Facultad, Espacio, facultad_equipo, Reserva, Comentarios, comentario_servicio

class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'fecha_solicitud',
        'id_equipo',
        'id_espacio',
        'detalle_reserva',
    )
    list_filter = (
        'fecha_solicitud',
    )
    search_fields = (
        'id_equipo',
        'id_espacio',
    )

class ComentariosAdmin(admin.ModelAdmin):
    list_display = (
        'id_reserva',
        'id_estado',
        'detalle_reserva',
    )

    list_filter = (
        'id_estado',
    )

class comentario_servicioAdmin(admin.ModelAdmin):
    list_display = (
        'id_estado',
        'detalle_servicio',
    )
    list_filter = (
        'id_estado',
    )


class facultad_equipoAdmin(admin.ModelAdmin):
    list_display = (
        'id_facultad',
        'id_equipo',
        'fecha_ingresado',
    )
    list_filter = (
        'fecha_ingresado',
        'id_facultad',
    )
    search_fields = (
        'id_equipo',
    )

admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Facultad)
admin.site.register(Espacio)
admin.site.register(facultad_equipo, facultad_equipoAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(comentario_servicio, comentario_servicioAdmin)
#