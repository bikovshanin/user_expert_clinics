from rest_framework import generics, serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from custom_auth.api.serializers import CustomTokenSerializer
from users.api.serializers import (MailUserSerializer, MobileUserSerializer,
                                   WebUserSerializer)
from users.models import User


class CustomTokenView(generics.CreateAPIView):
    """
    Представление для создания JWT-токенов.

    Методы:
        create: Создает и возвращает JWT-токены.
    """

    serializer_class = CustomTokenSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    """
    Представление для регистрации нового пользователя.

    Методы:
        get_serializer_class: Определяет сериализатор в зависимости от
        заголовка 'x-Device'.
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        device_type = self.request.headers.get('x-Device')

        if device_type == 'mail':
            return MailUserSerializer
        elif device_type == 'mobile':
            return MobileUserSerializer
        elif device_type == 'web':
            return WebUserSerializer
        else:
            raise serializers.ValidationError('Invalid x-Device header value.')
