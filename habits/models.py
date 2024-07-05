from django.db import models
from config import settings
from django.utils.translation import gettext as _

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Модель привычки"""
    class PeriodicityOfHabit(models.TextChoices):
        ONE = '1', _('Ежедневно')
        TWO = '2', _('Раз в 2 дня')
        THREE = '3', _('Раз в 3 дня')
        FOUR = '4', _('Раз в 4 дня')
        FIVE = '5', _('Раз в 5 дней')
        SIX = '6', _('Раз в 6 дней')
        SEVEN = '7', _('Раз в 7 дней')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='Пользователь')
    place = models.CharField(max_length=160, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=160, verbose_name='Действие')
    is_nice_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='Связанная привычка')
    periodicity = models.CharField(default=PeriodicityOfHabit.ONE, choices=PeriodicityOfHabit.choices,
                                   verbose_name='Периодичность')
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    duration_time = models.PositiveIntegerField(default=120, verbose_name='Время на выполнение (сек)')
    is_published = models.BooleanField(default=True, verbose_name='Признак публичности привычки')
    next_date = models.DateField(**NULLABLE, verbose_name='Дата следующего выполнения привычки')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['action']
