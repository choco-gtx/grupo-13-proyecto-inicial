from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('descubrir/', views.generar_lista, name='generar_lista'),
]