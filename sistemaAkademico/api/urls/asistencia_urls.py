# api/urls/asistencia_urls.py

from django.urls import path
from api.views.asistencia_views import MiVistaDeAsistencia  # Asegúrate de que esta vista exista

urlpatterns = [
    path('registrar/', MiVistaDeAsistencia.as_view(), name='registrar-asistencia'),
    # Agrega más rutas relacionadas con asistencia aquí
]
