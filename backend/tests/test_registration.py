from http import HTTPStatus

import pytest


@pytest.mark.django_db
class TestRegistrationAPI:

    def test_register_user_with_email(self, client, registration_data_email):
        """
        Тест для регистрации пользователя с использованием email.
        Проверяет, что регистрация проходит успешно и возвращается
        правильный статус и данные.
        """
        response = client.post(
            '/api/v1/auth/register/',
            data=registration_data_email,
            HTTP_X_DEVICE='mail'
        )
        assert response.status_code == HTTPStatus.CREATED, (
            'Регистрация пользователя с email должна возвращать '
            'статус 201 Created.'
            ' Проверьте правильность данных регистрации.'
        )
        response_data = response.json()
        assert response_data.get('email') == registration_data_email[
            'email'], (
            'Email в ответе не совпадает с ожидаемым.'
        )
        assert 'id' in response_data, (
            'В ответе должны быть возвращены данные '
            'пользователя с идентификатором.'
        )

    def test_register_user_with_phone(self, client, registration_data_phone):
        """
        Тест для регистрации пользователя с использованием номера телефона.
        Проверяет, что регистрация проходит успешно и возвращается
        правильный статус и данные.
        """
        response = client.post(
            '/api/v1/auth/register/',
            data=registration_data_phone,
            HTTP_X_DEVICE='mobile'
        )
        assert response.status_code == HTTPStatus.CREATED, (
            'Регистрация пользователя с номером телефона должна '
            'возвращать статус 201 Created.'
            ' Проверьте правильность данных регистрации.'
        )
        response_data = response.json()
        assert response_data.get('phone_number') == registration_data_phone[
            'phone_number'], (
            'Номер телефона в ответе не совпадает с ожидаемым.'
        )
        assert 'id' in response_data, (
            'В ответе должны быть возвращены данные '
            'пользователя с идентификатором.'
        )

    def test_register_user_with_invalid_data(self, client):
        """
        Тест для регистрации пользователя с некорректными данными.
        Проверяет, что регистрация с некорректными данными возвращает
        статус 400 Bad Request и соответствующие ошибки валидации.
        """
        response = client.post(
            '/api/v1/auth/register/',
            data={
                'email': 'invalidemail',
                'first_name': '',
                'last_name': '',
                'date_of_birth': 'not-a-date',
            },
            HTTP_X_DEVICE='mail'
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Регистрация с некорректными данными должна '
            'возвращать статус 400 Bad Request.'
        )
        response_data = response.json()
        assert 'email' in response_data, (
            'Ошибка валидации для email должна присутствовать в ответе.'
        )
        assert 'first_name' in response_data, (
            'Ошибка валидации для first_name должна присутствовать в ответе.'
        )
        assert 'date_of_birth' in response_data, (
            'Ошибка валидации для date_of_birth должна '
            'присутствовать в ответе.'
        )

    def test_register_user_with_missing_fields(self, client):
        """
        Тест для регистрации пользователя с отсутствующими
        обязательными полями.
        Проверяет, что регистрация с отсутствующими полями
        возвращает статус 400 Bad Request и
        ошибки валидации для отсутствующих полей.
        """
        response = client.post(
            '/api/v1/auth/register/',
            data={
                'phone_number': '+79114448989',
                'password': 'securepassword123',
            },
            HTTP_X_DEVICE='web'
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Регистрация с отсутствующими обязательными полями '
            'должна возвращать статус 400 Bad Request.'
        )
        response_data = response.json()
        assert 'first_name' in response_data, (
            'Ошибка валидации для first_name должна присутствовать в ответе.'
        )
        assert 'middle_name' in response_data, (
            'Ошибка валидации для middle_name должна присутствовать в ответе.'
        )
        assert 'last_name' in response_data, (
            'Ошибка валидации для last_name должна присутствовать в ответе.'
        )
        assert 'date_of_birth' in response_data, (
            'Ошибка валидации для date_of_birth должна '
            'присутствовать в ответе.'
        )
        assert 'passport_number' in response_data, (
            'Ошибка валидации для passport_number должна '
            'присутствовать в ответе.'
        )
        assert 'place_of_birth' in response_data, (
            'Ошибка валидации для place_of_birth должна '
            'присутствовать в ответе.'
        )
        assert 'registration_address' in response_data, (
            'Ошибка валидации для registration_address должна '
            'присутствовать в ответе.'
        )
