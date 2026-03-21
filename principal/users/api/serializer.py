from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'password',
        ]
    
    def validate_email(self, value):
        """Validar que el email sea único"""
        user = self.instance
        # Si es actualización y el email no cambió, permitir
        if user and user.email == value:
            return value
        # Si el email ya existe, lanzar error
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value