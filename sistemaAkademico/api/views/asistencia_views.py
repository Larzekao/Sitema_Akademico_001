# api/views/asistencia_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MiVistaDeAsistencia(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Lógica para registrar asistencia
        return Response({"mensaje": "Asistencia registrada correctamente"})
