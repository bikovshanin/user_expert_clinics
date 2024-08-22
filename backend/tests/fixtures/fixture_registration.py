import pytest


@pytest.fixture
def registration_data_email():
    """
        Фикстура для данных регистрации пользователя с использованием email.
        Возвращает словарь с email, паролем и именем пользователя.
        """
    return {
        'email': 'newuser@example.com',
        'password': 'securepassword123',
        'first_name': 'John'
    }


@pytest.fixture
def registration_data_phone():
    """
        Фикстура для данных регистрации пользователя с
        использованием номера телефона.
        Возвращает словарь с номером телефона и паролем.
        """
    return {
        'phone_number': '+79234567890',
        'password': 'securepassword123',
    }
