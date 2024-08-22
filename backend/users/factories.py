from django.contrib.auth.hashers import make_password
from factory import django, Faker

from users.models import User


class UserAdminFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'admin'
    last_name = 'adminov'
    middle_name = 'adminovich'
    phone_number = '+79991112233'
    email = 'admin@admin.ru'
    password = make_password('admin')
    is_staff = True
    is_superuser = True


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker('first_name_male')
    last_name = Faker('last_name_male')
    middle_name = Faker('middle_name_male')
    phone_number = Faker('phone_number')
    date_of_birth = Faker('date_of_birth', minimum_age=18, maximum_age=90)
    passport_number = Faker('numerify', text='#### ######')
    place_of_birth = Faker('city_name')
    registration_address = Faker('address')
    residence_address = registration_address
    email = Faker('email')
    password = make_password('test')
    is_staff = False
    is_superuser = False
