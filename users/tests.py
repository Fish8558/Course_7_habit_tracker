from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="Тестовый",
            email="test@test.ru",
            telegram_chat_id=123456789,
            is_active=True,
        )
        self.user.set_password('t1e2s3t')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        response = self.client.get(reverse('users:user-list'))
        data = response.json()
        result = [{'id': self.user.pk,
                   'name': 'Тестовый',
                   'email': 'test@test.ru',
                   'is_active': True,
                   'telegram_chat_id': '123456789'}, ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_user_create(self):
        data = {
            "name": "Максим",
            "email": "max-test@test.ru",
            "telegram_chat_id": 11223344,
            "password": 'qwe123test'
        }
        response = self.client.post(reverse('users:user-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_update(self):
        field = {"name": "Василий",
                 "password": 'q1w1e9870'}
        response = self.client.patch(reverse('users:user-detail', kwargs={"pk": self.user.pk}), field)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Василий")

    def test_user_retrieve(self):
        response = self.client.get(reverse('users:user-detail', kwargs={"pk": self.user.pk}))
        data = response.json()
        result = {'id': self.user.pk,
                  'name': 'Тестовый',
                  'email': 'test@test.ru',
                  'is_active': True,
                  'telegram_chat_id': '123456789'}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
        self.assertEqual(str(User.objects.get(email="test@test.ru")), "test@test.ru")

    def test_user_destroy(self):
        response = self.client.delete(reverse('users:user-detail', kwargs={"pk": self.user.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
