"""
URL configuration for sistemaAkademico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from .views import home_view  # Importa la vista
from .views import admin_view
from .views import profesor_view
from usuarios.views import admin_page, profesor_page, estudiante_page, tutor_page
urlpatterns = [
    path('', home_view, name='home'),  # Ruta raíz para la página de login,
   path('admin/', admin_page, name='admin_page'),
    path('profesor/', profesor_page, name='profesor_page'),
    path('estudiante/', estudiante_page, name='estudiante_page'),
    path('tutor/', tutor_page, name='tutor_page'),
   
    path('api/', include('api.urls')),  # Aqí incluyes todas las rutas de la app api
]
