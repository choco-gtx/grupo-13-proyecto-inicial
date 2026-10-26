import random
from django.shortcuts import render

def home(request):
    return render(request, "boton_descubrir/home.html")

def generar_lista(request):
    patrimonios = [
        {
            "patrimonio": 1,
            "ubicacion": "Ubicacion_1",
            "precio": 250000,
            "filtro_estudiante": True
        },
        {
            "patrimonio": 2,
            "ubicacion": "Ubicacion_2",
            "precio": 340000,
            "filtro_estudiante": False
        },
        {
            "patrimonio": 3,
            "ubicacion": "Ubicacion_3",
            "precio": 430000,
            "filtro_estudiante": True
        }
    ]

    random.shuffle(patrimonios)

    return render(request, "boton_descubrir/lista.html", {"datos": patrimonios})