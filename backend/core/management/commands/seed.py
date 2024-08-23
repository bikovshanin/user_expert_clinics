import logging

from django.core.management.base import BaseCommand
from django.db.models import Model

from users.factories import UserAdminFactory, UserFactory
from users.models import User

logger = logging.getLogger()


class Command(BaseCommand):
    """
    Команда Django для генерации тестовых данных.

    Использует фабрики для создания тестовых пользователей в базе данных.
    Удаляет все объекты указанных моделей перед генерацией новых данных.

    """
    help = 'Test data generation'

    FACTORIES = {
        UserAdminFactory: 1,
        UserFactory: 10,
    }

    MODELS = (
        User,
    )

    def clean_db(self, models: [Model]) -> None:
        for model in models:
            model.objects.all().delete()

    def seed_data(self, factories: dict) -> None:
        for factory, amount in factories.items():
            for _ in range(amount):
                factory()

    def handle(self, *args, **options):
        try:
            self.clean_db(self.MODELS)
            self.seed_data(self.FACTORIES)
        except Exception as e:
            logger.error(f'An error occurred during data generation: {e}')
            raise e
        else:
            logger.info('Test data generation was successful.')
