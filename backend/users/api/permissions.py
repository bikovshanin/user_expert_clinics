from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthenticatedOwnerOrAdmin(BasePermission):
    """
    Кастомное разрешение, позволяющее доступ только аутентифицированным
    пользователям,
    которые являются владельцами объекта или администраторами.

    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.is_staff:
            return True
        return request.method in SAFE_METHODS
