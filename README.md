# User and Authentication API

## Описание

Этот проект представляет собой API для управления пользователями и
аутентификации. Включает функции регистрации, аутентификации и управления
пользователями.

## Функционал

1. **Регистрация пользователя**:
    - Возможность регистрации по email, номеру телефона или с помощью
      web-формы.
2. **Аутентификация**:
    - Получение JWT токенов для авторизации.
    - Обновление токенов.
3. **Управление пользователями**:
    - Получение списка пользователей.
    - Получение детальной информации о пользователе.
    - Редактирование и удаление аккаунтов.

## Используемые технологии

[![pre-commit](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3111/)
[![pre-commit](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)
[![pre-commit](https://img.shields.io/badge/Django_REST_framework-3.15-800000?logo=djangorestramework&logoColor=white)](https://www.django-rest-framework.org/community/3.12-announcement/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Начало работы:

1. **Установка:** Клонируйте репозиторий на свой локальный компьютер.
2. **Настройка окружения:** В корневом каталоге проекта создайте файл `.env`. Вы
   можете использовать предоставленный файл `.env.example` в качестве шаблона.
   Убедитесь, что заполнили необходимые переменные окружения своими
   настройками.
3. **Docker Compose:** Перейдите в каталог проекта и выполните следующие
   команды, чтобы запустить приложение с использованием Docker Compose

```bash
docker compose up --build
```

4. **Доступ к приложению:** После того, как Docker Compose закончит настройку
   окружения, вы сможете получить доступ к документации, перейдя по
   адресу http://127.0.0.1/redoc/.
   Для доступа к админ-зоне пройдите по адресу http://127.0.0.1/admin/,
   суперпользователь создаётся автоматически (`логин: admin@admin.ru, пароль:
   admin`) Так же генерируются тестовые данные (10 пользователей).
## Использование API

### Регистрация пользователя

- **Endpoint**: `/api/v1/auth/register/`
- **Метод**: `POST`
- **Описание**: Создание нового пользователя. Можно зарегистрироваться через
  email, номер телефона или web-форму.

#### Примеры запросов:

**MailUser**:

```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

**MobileUser**:
```json
{
  "phone_number": "+79021234567",
  "password": "yourpassword"
}
```

**WebUser**:

```json
{
   "first_name": "Иван",
   "last_name": "Иванов",
   "middle_name": "Иванович",
   "date_of_birth": "1990-01-01",
   "passport_number": "1234 567890",
   "place_of_birth": "Москва",
   "phone_number": "+79234567890",
   "residence_address": "ул. Примерная, д. 1",
   "password": "yourpassword"
}
```

### Получение токена

- **Endpoint**: `/api/v1/auth/token/`
- **Метод**: `POST`
- **Описание**: Аутентификация пользователя по email или номеру телефона для
  получения JWT токена.

#### Пример запроса:

```json
{
   "email": "user@example.com",
   "password": "yourpassword"
}
```

### Обновление токена

- **Endpoint**: `/api/v1/auth/token/refresh/`
- **Метод**: `POST`
- **Описание**: Обновление токена доступа по рефреш-токену.

#### Пример запроса:

```json
{
   "refresh": "your-refresh-token"
}
```

### Список пользователей

- **Endpoint**: `/api/v1/users/`
- **Метод**: `GET`
- **Описание**: Возвращает список всех пользователей. Доступно только
  авторизованным пользователям.

### Получение информации о пользователе

- **Endpoint**: `/api/v1/users/{id}/`
- **Метод**: `GET`
- **Описание**: Возвращает детальную информацию о пользователе. Доступно авторизованным пользователям (только свои данные) и администраторам (любой аккаунт).

### Обновление пользователя

- **Endpoint**: `/api/v1/users/{id}/`
- **Методы**: `PUT` или `PATCH`
- **Описание**: Обновление информации о пользователе. PUT для полного
  обновления, PATCH для частичного обновления. Доступно только владельцу
  аккаунта и администраторам.

### Удаление пользователя

- **Endpoint**: `/api/v1/users/{id}/`
- **Метод**: `DELETE`
- **Описание**: Удаляет пользователя по его ID. Доступно только владельцу
  аккаунта и администраторам.

### Авторизация

Для доступа к защищенным ресурсам необходимо предоставлять JWT токен в
заголовке `Authorization` запроса в формате `Bearer <token>`.


