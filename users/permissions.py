from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка на владельца"""
    message = "Доступно только владельцу!"

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsOwnerHabit(BasePermission):
    """Проверка на создателя привычки"""
    message = "Вы не создатель!"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
