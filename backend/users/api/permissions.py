from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedOwnerOrAdmin(BasePermission):
    """
    Custom permission to check if the user is authenticated
    and either the owner of the object or an admin.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.is_staff:
            return True
        return request.method in SAFE_METHODS
