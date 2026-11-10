from django.contrib import admin
from .models import Patrimonio, SolicitudPatrimonio

admin.site.register(Patrimonio)  #Registramos el modelo Patrimonio en el sitio web de admin


# Presionar save guarda la solicitud del usuario como un patrimonio nuevo y borra la solicitud
class SolicitudPatrimonioAdmin(admin.ModelAdmin):

    # Presionar save
    def save_model(self, request, obj, form, change):

        # Guarda la solicitud normalmente
        super().save_model(request, obj, form, change)

        # Crea un patrimonio utilizando los datos de la solicitud
        Patrimonio.objects.create(
            nombre=obj.nombre,
            descripcion=obj.descripcion,
            ubicacion=obj.ubicacion,
            precio=obj.precio,
            filtro_estudiante=obj.filtro_estudiante,
            comida_cerca=obj.comida_cerca,
            horario=obj.horario,
            link_maps=obj.link_maps,
            imagen=obj.imagen
        )

        # Indica que la solicitud ya fue añadida
        obj.nombre = obj.nombre + " [AÑADIDO]"
        obj.save()

admin.site.register(SolicitudPatrimonio, SolicitudPatrimonioAdmin)