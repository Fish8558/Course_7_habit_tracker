from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="Тестовый",
            email="test@test.ru",
            telegram_chat_id=123456789,
            is_active=True
        )
        self.user.set_password('t1e2s3t')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Парк",
            time="18:00",
            action="Пробежка",
            periodicity="2",
            reward="Выпить воды",
            duration_time=120
        )

    def test_habit_create(self):
        data = {
            "place": "Офис",
            "time": "9:00",
            "action": "Программировать",
            "periodicity": "1",
            "reward": "Зарплата",
            "duration_time": 100
        }
        response = self.client.post(reverse('habits:habit_create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        response = self.client.get(reverse('habits:habit_list'))
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {'id': self.habit.pk,
                       'duration_time': 120,
                       'periodicity': '2',
                       'place': 'Парк',
                       'time': '18:00:00',
                       'action': 'Пробежка',
                       'is_nice_habit': False,
                       'reward': 'Выпить воды',
                       'is_published': True,
                       'next_date': None,
                       'user': self.user.pk,
                       'related_habit': None}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_owner_list(self):
        response = self.client.get(reverse('habits:habit_user_list'))
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {'id': self.habit.pk,
                       'duration_time': 120,
                       'periodicity': '2',
                       'place': 'Парк',
                       'time': '18:00:00',
                       'action': 'Пробежка',
                       'is_nice_habit': False,
                       'reward': 'Выпить воды',
                       'is_published': True,
                       'next_date': None,
                       'user': self.user.pk,
                       'related_habit': None}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_retrieve(self):
        response = self.client.get(reverse('habits:habit_detail', args=(self.habit.pk,)))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["place"], self.habit.place)
        self.assertEqual(str(Habit.objects.get(user=self.user.pk)), "Пробежка")

    def test_habit_update(self):
        field = {"reward": "Сходить в душ"}
        response = self.client.patch(reverse('habits:habit_update', args=(self.habit.pk,)), field)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["reward"], "Сходить в душ")

    def test_habit_destroy(self):
        response = self.client.delete(reverse('habits:habit_delete', args=(self.habit.pk,)))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
