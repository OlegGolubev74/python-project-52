from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User

class UserTest(TestCase):
    fixtures = ['users_data.json']

    def setUp(self):
        # Берем первого пользователя из фикстуры
        self.user = User.objects.first()
        self.client.force_login(self.user)

    def test_users_list(self):
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_user_create(self):
        self.client.logout()
        data = {
            'username': 'new_user_77',
            'first_name': 'Ivan77',
            'last_name': 'Ivanov77',
            'password1': 'pass12345',
            'password2': 'pass12345',
        }
        response = self.client.post(reverse('user_create'), data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='new_user_77').exists())

    def test_user_update(self):
        url = reverse('user_update', kwargs={'pk': self.user.pk})
        new_data = {
            'username': 'updated_oleg',
            'first_name': 'Олег',
            'last_name': 'Голубев',
        }
        response = self.client.post(url, new_data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updated_oleg')
        self.assertRedirects(response, reverse('users_list'))

    def test_user_delete_self(self):
        url = reverse('user_delete', kwargs={'pk': self.user.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('users_list'))
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
