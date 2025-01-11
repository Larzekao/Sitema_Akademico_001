from rest_framework import serializers
from usuarios.models import Usuario  # o el modelo que uses

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol']  
        # Ajusta según tus campos (e.g. 'nombre', 'apellido', etc.)

class UsuarioCreateSerializer(serializers.ModelSerializer):
    """ Serializador para crear usuarios, 
        puede incluir validación extra o campos como password. """
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'rol']
        extra_kwargs = {
            'password': {'write_only': True}  # no se devuelva la password en GET
        }

    def create(self, validated_data):
        # Manejo de creación con password encriptada
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            rol=validated_data['rol']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
