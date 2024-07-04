from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@site.com',
            name='Admin',
            telegram_chat_id='01233210',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('qwe123qwe321')
        user.save()
