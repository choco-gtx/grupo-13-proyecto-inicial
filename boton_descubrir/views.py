import random
from django.shortcuts import render  # Las páginas HTML que se muestran al usuario

def home(request):  
    return render(request, "boton_descubrir/home.html")  # Render indica que debe mostrar la página "home" al usuario

def generar_lista(request):  # Función que aleatoriza la lista de patrimonios
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

    random.shuffle(patrimonios)  # Aleatoriza

    return render(request, "boton_descubrir/lista.html", {"datos": patrimonios})
    # Se muestra la sección de la lista.html ocupando "datos = patrimonios" en ella