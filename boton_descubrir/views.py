import random
from django.shortcuts import render, redirect  # Las páginas HTML que se muestran al usuario
from django.contrib import messages
from .models import Patrimonio  # El modelo creado en models.py
from .forms import SolicitudPatrimonioForm  # El modelo de la solicitud de patrimonio.

def home(request):  
    return render(request, "boton_descubrir/home.html")  # Render indica que debe mostrar la página "home" al usuario

def generar_lista(request):  # Función que aleatoriza la lista de patrimonios
    patrimonios = list(Patrimonio.objects.all())  # La lista son todos los objetos del modelo Patrimonio (SQLite)


    # Verificación de si se presionó Descubrir o Reintentar (evitar reinicio lista presionando filtros)
    nuevo = request.GET.get("nuevo") == "1"

    if nuevo or "patrimonios" not in request.session:  # Se presionó el botón o aún no existe la lista
        random.shuffle(patrimonios)  # Aleatoriza
        request.session["patrimonios"] = [p.id for p in patrimonios]  # Guarda los ID de los patrimonios aleatorizados.

    else:  # Se activó un filtro (no se está pidiendo una nueva lista)
        ids = request.session["patrimonios"]  # "ids" son los identificadores de cada patrimonio
        patrimonios = [Patrimonio.objects.get(id=ident) for ident in ids]  # Busca cada patrimonio que corresponde a cada ID



    # Verificación de si el checkbox está activado o no (El checkbox tiene como valor "1", por eso el == "1")
    # Retorna True o False en las variables
    gratuito = request.GET.get("gratuito") == "1" 
    estudiantes = request.GET.get("estudiantes") == "1"
    comida = request.GET.get("comida") == "1"

    mostrar_filtros = request.GET.get("mostrar_filtros") == "1"

    if gratuito:
        patrimonios = [p for p in patrimonios if p.precio == 0]  # Forma simplificada de recorrer todos los patrimonios
    if estudiantes:
        patrimonios = [p for p in patrimonios if p.filtro_estudiante]
    if comida:
        patrimonios = [p for p in patrimonios if p.comida_cerca]


    # Se muestra la sección de la lista.html ocupando "datos = patrimonios" en ella
    return render(request, "boton_descubrir/lista.html", {"datos": patrimonios, 
        "gratuito": gratuito,
        "estudiantes": estudiantes,
        "comida": comida,
        "mostrar_filtros": mostrar_filtros})


def solicitud(request):  
    formulario = SolicitudPatrimonioForm()  # Crea el formulario vacío

    if request.method == "POST":  # Comprobar si el usuario lo envió
        formulario = SolicitudPatrimonioForm(request.POST)

        if formulario.is_valid():  # Comprueba la validez de los datos
            formulario.save()
            messages.success(request, "¡Solicitud enviada correctamente!")
            return redirect("solicitud")
        
    return render(request, "boton_descubrir/solicitud.html", {
        "formulario": formulario
    })