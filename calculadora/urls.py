from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular, name='metodo'),  # Usamos la función correcta
]
