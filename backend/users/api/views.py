from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated

from users.models import User

from .permissions import IsAuthenticatedOwnerOrAdmin
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    """
    Представление для получения списка пользователей.

    Доступно только для аутентифицированных пользователей.

    Атрибуты:
        queryset (QuerySet): Запрос всех объектов пользователей.
        serializer_class (Serializer): Сериализатор для пользователя.
        permission_classes (tuple): Кортеж с классами разрешений.
        filter_backends (tuple): Кортеж с классами фильтров.
        search_fields (tuple): Кортеж полей, по которым выполняется поиск.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'last_name',
        'first_name',
        'middle_name',
        'phone_number',
        'email',
    )


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления пользователя.

    Доступ:
        GET - доступно только для аутентифицированных пользователей.
        PUT, PATCH, DELETE - только для владельца объекта или администратора.

    Атрибуты:
        queryset (QuerySet): Запрос всех объектов пользователей.
        serializer_class (Serializer): Сериализатор для пользователя.
        permission_classes (tuple): Кортеж с классами разрешений.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOwnerOrAdmin,)
