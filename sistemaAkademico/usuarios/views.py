from django.shortcuts import render

def admin_page(request):
    return render(request, 'admin.html')

def profesor_page(request):
    return render(request, 'profesor.html')

def estudiante_page(request):
    return render(request, 'estudiante.html')

def tutor_page(request):
    return render(request, 'tutor.html')