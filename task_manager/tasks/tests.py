from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskTest(TestCase):
    fixtures = [
        'users_data.json',
        'statuses_data.json',
        'labels_data.json',
        'tasks_data.json',
    ]

    def setUp(self):
        self.user = User.objects.first()
        self.status = Status.objects.first()
        self.task = Task.objects.first()
        self.label = Label.objects.first()
        
        self.client.force_login(self.user)

    def test_task_detail(self):
        url = reverse('task_detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)

    def test_task_create_with_label(self):
        data = {
            'name': 'Новая задача',
            'status': self.status.pk,
            'executor': self.user.pk,
            'description': 'Описание',
            'labels': [self.label.pk]
        }
        response = self.client.post(reverse('task_create'), data)
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertTrue(Task.objects.filter(name='Новая задача').exists())

    def test_task_delete_by_author(self):
        # проверка удаления своей задачи
        url = reverse('task_delete', kwargs={'pk': self.task.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_delete_by_other_fails(self):
        # проверка неудачи удаления чужой задачи
        other_user = User.objects.get(pk=2)
        self.client.force_login(other_user)
        
        url = reverse('task_delete', kwargs={'pk': self.task.pk})
        response = self.client.post(url)
        
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertTrue(Task.objects.filter(pk=self.task.pk).exists())

    # проверки для шага 7
    def test_filter_tasks_by_status(self):
        # проверяем, что в списке только задачи со статусом pk=1
        url = reverse('tasks_list') + '?status=1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        for task in response.context['tasks']:
            self.assertEqual(task.status.pk, 1)