# usuarios/urls.py (o donde definas tus rutas)
from django.urls import path
from .views import admin_page, profesor_page, estudiante_page, tutor_page

urlpatterns = [
    path('admin/', admin_page, name='admin_page'),
    path('profesor-page/', profesor_page, name='profesor_page'),
    path('estudiante-page/', estudiante_page, name='estudiante_page'),
    path('tutor-page/', tutor_page, name='tutor_page'),
]
