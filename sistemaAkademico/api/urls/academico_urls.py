# api/urls/academico_urls.py

from django.urls import path
from api.views.academico_views import MiVistaDeEjemplo  # Asegúrate de que esta vista existe

urlpatterns = [
    path('ejemplo/', MiVistaDeEjemplo.as_view(), name='ejemplo-academico'),
    # Agrega más rutas relacionadas con académico aquí
]