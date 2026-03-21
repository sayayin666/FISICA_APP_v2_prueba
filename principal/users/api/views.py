from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.api.serializer import UserSerializer
from users.models import User
from django.contrib.auth.hashers import make_password

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        # Verificamos si la contraseña viene en la petición PATCH
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])
        
        return super().partial_update(request, *args, **kwargs)