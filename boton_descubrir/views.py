import random
from django.shortcuts import render  # Las páginas HTML que se muestran al usuario

def home(request):  
    return render(request, "boton_descubrir/home.html")  # Render indica que debe mostrar la página "home" al usuario

def generar_lista(request):  # Función que aleatoriza la lista de patrimonios
    patrimonios = [
        {
            "patrimonio": 1,
            "ubicacion": "Ubicacion_1",
            "precio": 0,
            "filtro_estudiante": True,
            "comida_cerca": True
        },
        {
            "patrimonio": 2,
            "ubicacion": "Ubicacion_2",
            "precio": 0,
            "filtro_estudiante": True,
            "comida_cerca": False
        },
        {
            "patrimonio": 3,
            "ubicacion": "Ubicacion_3",
            "precio": 0,
            "filtro_estudiante": False,
            "comida_cerca": False
        },
        {
            "patrimonio": 4,
            "ubicacion": "Ubicacion_4",
            "precio": 2400,
            "filtro_estudiante": False,
            "comida_cerca": True
        }
    ]

    # Verificación de si el checkbox está activado o no (El checkbox tiene como valor "1", por eso el == "1")
    # Retorna True o False en las variables
    gratuito = request.GET.get("gratuito") == "1" 
    estudiantes = request.GET.get("estudiantes") == "1"
    comida = request.GET.get("comida") == "1"

    random.shuffle(patrimonios)  # Aleatoriza

    if gratuito == True:
        patrimonios = [p for p in patrimonios if p["precio"] == 0]  # Forma simplificada de recorrer todos los patrimonios
    if estudiantes == True:
        patrimonios = [p for p in patrimonios if p["filtro_estudiante"] == True]
    if comida == True:
        patrimonios = [p for p in patrimonios if p["comida_cerca"] == True]

    return render(request, "boton_descubrir/lista.html", {"datos": patrimonios, 
        "gratuito": gratuito,
        "estudiantes": estudiantes,
        "comida": comida})
    # Se muestra la sección de la lista.html ocupando "datos = patrimonios" en ella