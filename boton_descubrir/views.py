import random
from django.shortcuts import render

def home(request):
    return render(request, "boton_descubrir/home.html")

def generar_lista(request):
    patrimonios = [
        {
            "patrimonio": 1,
            "ubicacion": "Ubicacion_1",
            "precio": 2100,
            "filtro_estudiante": True
        },
        {
            "patrimonio": 2,
            "ubicacion": "Ubicacion_2",
            "precio": 0,
            "filtro_estudiante": False
        },
        {
            "patrimonio": 3,
            "ubicacion": "Ubicacion_3",
            "precio": 4300,
            "filtro_estudiante": True
        },
        {
            "patrimonio": 4,
            "ubicacion": "Ubicacion_4",
            "precio": 2400,
            "filtro_estudiante": False
        }
    ]

    random.shuffle(patrimonios)

    return render(request, "boton_descubrir/lista.html", {"datos": patrimonios})