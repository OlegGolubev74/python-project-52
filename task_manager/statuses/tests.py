from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User

class StatusTest(TestCase):
    fixtures = ['statuses_data.json']

    def setUp(self):
        self.user = User.objects.create_user(username='test_user123', password='password123')
        self.client.force_login(self.user)
        
        self.status = Status.objects.first()

    def test_access_list_only_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('statuses_list'))
        self.assertEqual(response.status_code, 302)

    def test_statuses_list(self):
        response = self.client.get(reverse('statuses_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.name)

    def test_status_create(self):
        url = reverse('status_create')
        data = {'name': 'Новый созданный статус'}
        response = self.client.post(url, data)
        
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertTrue(Status.objects.filter(name='Новый созданный статус').exists())

    def test_status_update(self):
        url = reverse('status_update', kwargs={'pk': self.status.pk})
        new_data = {'name': 'Обновленное имя'}
        response = self.client.post(url, new_data)
        
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Обновленное имя')
        self.assertRedirects(response, reverse('statuses_list'))

    def test_status_delete(self):
        url = reverse('status_delete', kwargs={'pk': self.status.pk})
        response = self.client.post(url)
        
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
