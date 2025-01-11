# api/urls/__init__.py
from django.urls import path, include
from api.views.usuarios_views import login_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('usuarios/', include('api.urls.usuarios_urls')),
    path('academico/', include('api.urls.academico_urls')),
    path('asistencia/', include('api.urls.asistencia_urls')),
]