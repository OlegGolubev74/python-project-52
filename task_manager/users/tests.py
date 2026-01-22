from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User

class UserTest(TestCase):
    fixtures = ['users_data.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user) 

    def test_users_list(self):
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_user_create(self):
        self.client.logout()
        url = reverse('user_create')
        data = {
            'username': 'username74',
            'first_name': 'first_name74',
            'last_name': 'last_name74',
            'password1': 'password74',
            'password2': 'password74',
        }
        response = self.client.post(url, data)
        
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='username74').exists())

    def test_user_update(self):
        url = reverse('user_update', kwargs={'pk': self.user.pk})
        new_data = {
            'username': 'updated_name',
            'first_name': 'Oleg',
            'last_name': 'Golubev',
        }
        response = self.client.post(url, new_data)
        
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 302)  # Редирект после успеха
        self.assertEqual(self.user.username, 'updated_name')

    def test_user_delete(self):
        url = reverse('user_delete', kwargs={'pk': self.user.pk})
        response = self.client.post(url)
        
        self.assertRedirects(response, reverse('users_list'))
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

    def test_update_other_user(self):
        other_user = User.objects.create(username='other', password='123')
        url = reverse('user_update', kwargs={'pk': other_user.pk})
        
        response = self.client.post(url, {'username': 'new_username'})
        
        self.assertRedirects(response, reverse('users_list'))
        
        other_user.refresh_from_db()
        self.assertNotEqual(other_user.username, 'new_username')

