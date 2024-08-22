import re

from rest_framework import serializers

from backend.settings import PASSPORT_REGEX
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'last_name',
            'first_name',
            'middle_name',
            'date_of_birth',
            'passport_number',
            'place_of_birth',
            'phone_number',
            'registration_address',
            'residence_address',
            'password',
        )


class UserCreateSerializer(UserSerializer):
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_passport_number(self, value):
        if not re.match(PASSPORT_REGEX, value):
            raise serializers.ValidationError(
                'Passport number must be in the format "ХХХХ ХХХХХХ".')

        if User.objects.filter(passport_number=value).exists():
            raise serializers.ValidationError(
                'User with this passport number already exists.')
        return value

    def validate_email(self, value):
        print(value)
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'User with this email already exists.')
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                'User with this phone number already exists.')
        return value


class MailUserSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class MobileUserSerializer(UserCreateSerializer):
    phone_number = serializers.CharField(required=True)


class WebUserSerializer(UserCreateSerializer):

    def validate(self, data):
        required_fields = (
            'last_name',
            'first_name',
            'middle_name',
            'date_of_birth',
            'passport_number',
            'place_of_birth',
            'phone_number',
            'registration_address',
        )

        errors = {}
        for field in required_fields:
            if not data.get(field):
                errors[
                    field] = f"{field.replace('_', ' ').title()} is required."

        if errors:
            raise serializers.ValidationError(errors)

        return data
