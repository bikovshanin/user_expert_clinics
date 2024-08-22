from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from backend.settings import MAX_NAME_LENGTH


class CustomUserManager(BaseUserManager):
    """
    Custom manager for user model.
    """

    def _create_user(self, email=None, phone_number=None, password=None,
                     **extra_fields):
        if not email and not phone_number:
            raise ValueError('Either Email or Phone number must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number,
                          **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, phone_number=None, password=None,
                    **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone_number, password, **extra_fields)

    def create_superuser(self, email=None, phone_number=None, password=None,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not email:
            raise ValueError('Superuser must have an email.')
        return self._create_user(email, phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        'email',
        unique=True,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )
    date_of_birth = models.DateField(
        'Дата рождения',
        blank=True,
        null=True,
    )
    passport_number = models.CharField(
        'Номер паспорта',
        unique=True,
        max_length=11,
        blank=True,
        null=True,
    )
    place_of_birth = models.CharField(
        'Место рождения',
        max_length=255,
        blank=True,
        null=True,
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        unique=True,
        blank=True,
        null=True,
    )
    registration_address = models.TextField(
        'Адрес регистрации',
        blank=True,
        null=True,
    )
    residence_address = models.TextField(
        'Адрес проживания',
        blank=True,
        null=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = (
            'id',
            'email',
        )

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None
        if self.phone_number == '':
            self.phone_number = None
        elif self.phone_number:
            # Преобразование объекта PhoneNumber в строку для проверки
            phone_number_str = str(self.phone_number)
            if phone_number_str.startswith('8'):
                # Заменяем '8' на '+7' в начале номера телефона
                phone_number_str = '+7' + phone_number_str[1:]
                self.phone_number = phone_number_str
        super().save(*args, **kwargs)

    def __repr__(self):
        return f'User {self.id}'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
