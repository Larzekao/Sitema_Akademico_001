# sistemaAkademico/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'login.html')


def admin_view(request):
    return render(request, 'admin.html')


def profesor_view(request):
    return render(request, 'profesor.html')


def estudiante_view(request):
    return render(request, 'estudiante.html')

def tutor_view(request):
    return render(request, 'tutor.html')

