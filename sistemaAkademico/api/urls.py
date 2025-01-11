# api/urls.py
from django.urls import path, include

from api.views.usuarios_views import login_view
urlpatterns = [
     path('login/', login_view, name='login_api'),

]
