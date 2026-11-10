from django import forms
from .models import SolicitudPatrimonio

class SolicitudPatrimonioForm(forms.ModelForm):  # Crea un formulario SolicitudPatrimonio
    class Meta:
        model = SolicitudPatrimonio
        fields = [
            "nombre",
            "link_maps",
            "descripcion",
            "ubicacion",
            "precio",
            "filtro_estudiante",
            "comida_cerca",
            "horario",
            "imagen"
        ]