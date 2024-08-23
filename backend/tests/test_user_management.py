from http import HTTPStatus

import pytest

from users.models import User


@pytest.mark.django_db
class TestUserManagementAPI:

    def test_update_own_user(self, user_client, user):
        """
        Тест для обновления данных собственного пользователя.
        Проверяет, что обновление данных проходит
        успешно и возвращается правильный статус и данные.
        """
        response = user_client.put(
            f'/api/v1/users/{user.id}/',
            data={
                'first_name': 'UpdatedName',
                'last_name': 'UpdatedLastName'
            },
            format='json'
        )
        assert response.status_code == HTTPStatus.OK, (
            'Обновление данных собственного пользователя '
            'должно возвращать статус 200 OK.'
        )
        response_data = response.json()
        assert response_data.get('first_name') == 'UpdatedName', (
            'Имя пользователя в ответе не совпадает с ожидаемым.'
        )
        assert response_data.get('last_name') == 'UpdatedLastName', (
            'Фамилия пользователя в ответе не совпадает с ожидаемой.'
        )

    def test_update_user_as_admin(self, admin_client, user):
        """
        Тест для обновления данных пользователя администратором.
        Проверяет, что обновление данных проходит успешно
        и возвращается правильный статус и данные.
        """
        response = admin_client.put(
            f'/api/v1/users/{user.id}/',
            data={
                'first_name': 'AdminUpdatedName',
                'last_name': 'AdminUpdatedLastName'
            },
            format='json'
        )
        assert response.status_code == HTTPStatus.OK, (
            'Обновление данных пользователя администратором '
            'должно возвращать статус 200 OK.'
        )
        response_data = response.json()
        assert response_data.get('first_name') == 'AdminUpdatedName', (
            'Имя пользователя в ответе не совпадает с ожидаемым.'
        )
        assert response_data.get('last_name') == 'AdminUpdatedLastName', (
            'Фамилия пользователя в ответе не совпадает с ожидаемой.'
        )

    def test_update_user_unauthorized(self, user_client):
        """
        Тест для попытки обновления данных другого пользователя
        неавторизованным пользователем.
        Проверяет, что попытка обновления данных другого п
        ользователя возвращает статус 403 Forbidden.
        """
        other_user = User.objects.create_user(
            email='otheruser@example.com',
            password='otherpassword',
            first_name='Other',
            last_name='User'
        )
        response = user_client.put(
            f'/api/v1/users/{other_user.id}/',
            data={
                'first_name': 'UnauthorizedUpdate',
                'last_name': 'UnauthorizedUpdate'
            },
            format='json'
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            'Попытка обновления данных другого пользователя '
            'должна возвращать статус 403 Forbidden.'
        )

    def test_delete_user_as_admin(self, admin_client):
        """
        Тест для удаления пользователя администратором.
        Проверяет, что удаление пользователя проходит успешно и
        пользователь больше не существует.
        """
        other_user = User.objects.create_user(
            email='deletableuser@example.com',
            password='deletablepassword',
            first_name='Deletable',
            last_name='User'
        )
        response = admin_client.delete(f'/api/v1/users/{other_user.id}/')
        assert response.status_code == HTTPStatus.NO_CONTENT, (
            'Удаление пользователя администратором должно '
            'возвращать статус 204 No Content.'
        )
        assert not User.objects.filter(id=other_user.id).exists(), (
            'Пользователь должен быть удален из базы данных.'
        )

    def test_delete_user_unauthorized(self, user_client):
        """
        Тест для попытки удаления другого пользователя н
        еавторизованным пользователем.
        Проверяет, что попытка удаления другого пользователя
        возвращает статус 403 Forbidden.
        """
        other_user = User.objects.create_user(
            email='anotherdeletableuser@example.com',
            password='anotherdeletablepassword',
            first_name='AnotherDeletable',
            last_name='User'
        )
        response = user_client.delete(f'/api/v1/users/{other_user.id}/')
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            'Попытка удаления другого пользователя должна '
            'возвращать статус 403 Forbidden.'
        )
        assert User.objects.filter(id=other_user.id).exists(), (
            'Пользователь не должен быть удален из базы данных.'
        )
