from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User

class StatusTest(TestCase):
    fixtures = ['statuses_data.json', 'users_data.json']

    def setUp(self):
        self.user = User.objects.first()
        self.status = Status.objects.first()
        self.client.force_login(self.user)

    def test_statuses_list(self):
        response = self.client.get(reverse('statuses_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.name)

    def test_status_create(self):
        data = {'name': 'Тестовый статус'}
        response = self.client.post(reverse('status_create'), data)
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertTrue(Status.objects.filter(name='Тестовый статус').exists())

    def test_status_update(self):
        url = reverse('status_update', kwargs={'pk': self.status.pk})
        response = self.client.post(url, {'name': 'Изменено'})
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Изменено')

    def test_status_delete(self):
        temp_status = Status.objects.create(name='Удали меня')
        url = reverse('status_delete', kwargs={'pk': temp_status.pk})
        response = self.client.post(url)
        self.assertFalse(Status.objects.filter(name='Удали меня').exists())
