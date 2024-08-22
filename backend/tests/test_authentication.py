import pytest
from http import HTTPStatus


@pytest.mark.django_db
class TestAuthAPI:

    def test_token_obtain_with_email(self, client, user):
        response = client.post(
            '/api/v1/auth/token/',
            data={'email': user.email, 'password': 'userpassword'}
        )
        assert response.status_code == HTTPStatus.OK
        auth_data = response.json()
        assert 'refresh' in auth_data, (
            'В ответе должны быть возвращены данные токена refresh.'
        )
        assert 'access' in auth_data, (
            'В ответе должны быть возвращены данные токена access.'
        )

    def test_token_obtain_with_phone(self, client, user):
        """
        Тест для получения токена с использованием номера телефона.
        Проверяет, что получение токена проходит успешно и возвращается
        правильный статус и данные.
        """
        response = client.post(
            '/api/v1/auth/token/',
            data={'phone_number': user.phone_number,
                  'password': 'userpassword'}
        )
        assert response.status_code == HTTPStatus.OK, (
            'Получение токена по номеру телефона должно возвращать '
            'статус 200 OK.'
        )
        auth_data = response.json()
        assert 'refresh' in auth_data, (
            'В ответе должны быть возвращены данные токена refresh.'
        )
        assert 'access' in auth_data, (
            'В ответе должны быть возвращены данные токена access.'
        )

    def test_token_obtain_with_invalid_credentials(self, client):
        """
        Тест для получения токена с некорректными учетными данными.
        Проверяет, что попытка получения токена с неверными данными в
        озвращает статус 401 Unauthorized.
        """
        response = client.post(
            '/api/v1/auth/token/',
            data={'email': 'invalid@example.com', 'password': 'wrongpassword'}
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Попытка получения токена с некорректными данными должна '
            'возвращать статус 401 Unauthorized.'
        )
