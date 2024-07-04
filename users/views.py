from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer, UserInfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet работы с пользователями"""
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['retrieve', 'update', 'destroy', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            self.serializer_class = UserSerializer
        elif self.action in ['retrieve', 'list']:
            self.serializer_class = UserInfoSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
