from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('descubrir/', views.generar_lista, name='generar_lista'),
    path('solicitar/', views.solicitar_patrimonio, name='solicitar_patrimonio'),

    # La función path basicamente dice que cuando se visite la ruta (el primer parámetro),
    # se activará la función del segundo parámetro y a esta se le dará el nombre del tercero.
]