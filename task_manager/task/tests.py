from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Task


class TaskCRUDTest(TestCase):
    """Tests for task CRUD operation."""
    user_data = {
        'username': 'tota',
        'first_name': 'Tota',
        'last_name': 'Totavich',
        'password': 'adminadmin',
    }

    def setUp(self):
        """Set up test enviroment and login user."""
        self.client = Client()
        self.data = {
            'create': {
                'name': 'Example task',
                'description': 'This is example task',
                'status': 1,
                'executor': 1,
            },
            'update': {
                'name': 'Updated task',
                'description': 'This is updated task',
                'status': 2,
                'executor': 2,
            },
        }
        User.objects.create_user(**self.user_data)
        login_url = reverse('login')
        self.client.post(
            login_url,
            {
                'username': self.user_data['username'],
                'password': self.user_data['password']
            }
        )

    def test_create_task(self):
        """Test task creation on POST."""
        url = reverse('task_create')
        task_data = self.data['create']
        self.client.post(url, task_data)

        task = Task.objects.last()
        self.assertEqual(task.name, task_data['name'])
        self.assertEqual(task.description, task_data['description'])

    def test_read_task(self):
        """Test tasks index reading."""
        url = reverse('tasks_index')
        task_data = self.data['create']
        task = Task.objects.create(**task_data)

        response = self.client.get(url)
        content = response.content.decode('utf-8')
        self.assertIn(task.name, content)
        self.assertIn(task.description, content)

    def test_update_task(self):
        """Test task updation on POST."""
        task_data = self.data['create']
        task = Task.objects.create(**task_data)
        url = reverse('task_update', {'pk': task.pk})

        task_updated_data = self.data['updated']
        self.client.POST(url, task_updated_data)

        task_updated = Task.objects.get(pk=task.pk)
        self.assertEqual(task_updated.name, task_updated_data['name'])
        self.assertEqual(
            task_updated.description, task_updated_data['description']
        )

    def test_delete_task(self):
        """Test task deletion on POST."""
        task_data = self.data['create']
        task = Task.objects.create(**task_data)
        url = reverse('task_delete', {'pk': task.pk})

        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(pk=task.pk)
