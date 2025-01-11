

# api/urls/usuarios_urls.py

from django.urls import path

from api.views.usuarios_views import login_view

urlpatterns = [
   path('login/', login_view, name='login'),  # URL para la página de login
    # Puedes agregar más rutas relacionadas con usuarios aquí
]