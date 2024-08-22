import pytest
from rest_framework.test import APIClient

from users.models import User


@pytest.fixture
def user():
    """
    Фикстура для создания стандартного пользователя.
    Возвращает объект пользователя.
    """
    return User.objects.create_user(
        phone_number='+79023334455',
        email='user@example.com',
        password='userpassword',
        first_name='First',
        last_name='User'
    )


@pytest.fixture
def admin():
    """
    Фикстура для создания администратора.
    Возвращает объект администратора.
    """
    return User.objects.create_superuser(
        email='admin@example.com',
        password='adminpassword',
        first_name='Admin',
        last_name='User'
    )


@pytest.fixture
def api_client():
    """
    Фикстура для создания экземпляра APIClient.
    Возвращает объект APIClient.
    """
    return APIClient()


@pytest.fixture
def user_token(api_client, user):
    """
    Фикстура для получения токена пользователя.
    Возвращает токен доступа пользователя.
    """
    response = api_client.post('/api/v1/auth/token/', data={
        'email': user.email,
        'password': 'userpassword',
    })
    assert response.status_code == 200, (
        'Не удалось получить токен для пользователя. '
        'Проверьте корректность email и пароля.'
    )
    return response.data['access']


@pytest.fixture
def admin_token(api_client, admin):
    """
    Фикстура для получения токена администратора.
    Возвращает токен доступа администратора.
    """
    response = api_client.post('/api/v1/auth/token/', data={
        'email': admin.email,
        'password': 'adminpassword',
    })
    assert response.status_code == 200, (
        'Не удалось получить токен для администратора. '
        'Проверьте корректность email и пароля.'
    )
    return response.data['access']


@pytest.fixture
def user_client(api_client, user_token):
    """
    Фикстура для создания клиента API с авторизацией пользователя.
    Возвращает объект APIClient с установленным токеном доступа пользователя.
    """
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token}')
    return api_client


@pytest.fixture
def admin_client(api_client, admin_token):
    """
    Фикстура для создания клиента API с авторизацией администратора.
    Возвращает объект APIClient с установленным токеном доступа администратора.
    """
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {admin_token}')
    return api_client