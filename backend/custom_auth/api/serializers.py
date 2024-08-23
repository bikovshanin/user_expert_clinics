from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class CustomTokenSerializer(serializers.Serializer):
    """
    Сериализатор для создания JWT-токенов на основе email или номера телефона.

    Атрибуты:
        email (EmailField): Поле для email пользователя, опционально.
        phone_number (CharField): Поле для номера телефона пользователя,
        опционально.
        password (CharField): Поле для пароля пользователя, используется
        только для записи.
    """

    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        phone_number = data.get('phone_number')
        password = data.get('password')

        if not email and not phone_number:
            raise serializers.ValidationError(
                'Either email or phone number is required for authentication.'
            )

        user = None

        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise AuthenticationFailed(
                    'No user with this email found.'
                )

        elif phone_number:
            try:
                user = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                raise AuthenticationFailed(
                    'No user with this phone number found.'
                )

        if user and not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')

        if user is None:
            raise AuthenticationFailed('Invalid credentials.')

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'phone_number': str(user.phone_number),
            }
        }
