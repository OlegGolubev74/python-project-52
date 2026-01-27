from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label
from task_manager.users.models import User
from task_manager.tasks.models import Task

class LabelTest(TestCase):
    fixtures = ['users_data.json', 'statuses_data.json', 'labels_data.json', 'tasks_data.json']

    def setUp(self):
        # берем первого пользователя из фикстуры для авторизации
        self.user = User.objects.first()
        self.client.force_login(self.user)
        
        #  берем самую первую метку
        self.label = Label.objects.first()

    def test_labels_list(self):
        #страница со списком открывается 
        response = self.client.get(reverse('labels_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.label.name) #и метка там есть на странице

    def test_create_label(self):
        # новая метка создается
        data = {'name': 'Срочно'}
        response = self.client.post(reverse('label_create'), data)
        self.assertRedirects(response, reverse('labels_list'))
        self.assertTrue(Label.objects.filter(name='Срочно').exists())

    def test_update_label(self):
        # метка изменяется
        url = reverse('label_update', kwargs={'pk': self.label.pk})
        response = self.client.post(url, {'name': 'Новое Имя'})
        
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Новое Имя')
        self.assertRedirects(response, reverse('labels_list'))

    def test_delete_label_not_used(self):
        # Проверяем удаление свободнойметки
        # Создаем временную метку, и удаляем ее
        temp_label = Label.objects.create(name='Временная')
        url = reverse('label_delete', kwargs={'pk': temp_label.pk})
        response = self.client.post(url)
        
        self.assertFalse(Label.objects.filter(name='Временная').exists())

    def test_delete_label_used_in_task(self):
        # Проверяем, что не получится удалить связанную метку
        task = Task.objects.first()
        task.labels.add(self.label)
        
        url = reverse('label_delete', kwargs={'pk': self.label.pk})
        response = self.client.post(url)
        
        self.assertRedirects(response, reverse('labels_list'))
        self.assertTrue(Label.objects.filter(pk=self.label.pk).exists())
