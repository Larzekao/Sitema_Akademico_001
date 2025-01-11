from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from usuarios.models import Usuario
from api.serializers.usuarios_serializers import (
    UsuarioSerializer, 
    UsuarioCreateSerializer
)

class UsuarioListView(generics.ListAPIView):
    """ Lista todos los usuarios. 
        Solo accesible para usuarios autenticados (podrías restringir más). """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class UsuarioCreateView(generics.CreateAPIView):
    """ Crea un usuario. 
        Quizás solo un Admin debería poder hacerlo, por ejemplo. """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCreateSerializer
    permission_classes = [IsAdminUser]

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Ver, actualizar o eliminar un usuario específico por ID. """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # usuario autenticado
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'rol': getattr(user, 'rol', None),    # En caso de que tu user tenga el campo rol
            'username': user.username
        })
    


# api/views/login_views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth import authenticate

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            # Verifica qué datos llegan al backend
            print("Datos recibidos (cuerpo del POST):", request.body.decode('utf-8'))

            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')

            print(f"Username recibido: {username}")
            print(f"Password recibido: {password}")

            try:
                user = Usuario.objects.get(username=username)
                print(f"Password en BD: {user.contrasena}")

                if user.contrasena == password:
                    print("Contraseña válida")
                    return JsonResponse({
                        "success": True,
                        "message": "Login exitoso",
                        "rol": user.rol
                    })
                else:
                    print("Contraseña incorrecta")
                    return JsonResponse({
                        "success": False,
                        "message": "Contraseña incorrecta"
                    }, status=401)

            except Usuario.DoesNotExist:
                print("Usuario no encontrado")
                return JsonResponse({
                    "success": False,
                    "message": "Usuario no encontrado"
                }, status=404)

        except Exception as e:
            print(f"Error interno: {e}")
            return JsonResponse({
                "success": False,
                "message": f"Error interno: {str(e)}"
            }, status=500)

    return JsonResponse({"message": "Método no permitido"}, status=405)

