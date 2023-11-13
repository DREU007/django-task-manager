from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from task_manager.status.models import Status
from .models import Task


class TaskCRUDTest(TestCase):
    """Tests for task CRUD operation."""

    @classmethod
    def setUpTestData(cls):
        """Set up data for tests."""
        cls.client = Client()
        user_data = {
            'user1': {
                'username': 'tota',
                'first_name': 'Tota',
                'last_name': 'Totavich',
                'password': 'adminadmin',
            },
            'user2': {
                'username': 'dada',
                'first_name': 'Dada',
                'last_name': 'Dadavich',
                'password': 'adminadmin',
            },
        }

        cls.author = User.objects.create_user(**user_data['user1'])
        cls.executor = User.objects.create_user(**user_data['user2'])

        login_url = reverse('login')
        cls.client.post(
            login_url,
            {
                'username': user_data['user1']['username'],
                'password': user_data['user2']['password']
            }
        )

        status_data = {
            'create': {'name': 'Example status'},
            'update': {'name': 'Updated status'},
        }
        cls.status1 = Status.objects.create(**status_data['create'])
        cls.status2 = Status.objects.create(**status_data['update'])

    def setUp(self):
        """Set up test enviroment and login user."""

        self.data = {
            'create': {
                'name': 'Example task',
                'description': 'This is example task',
                'status': self.status1,
                'executor': self.author,
            },
            'update': {
                'name': 'Updated task',
                'description': 'This is updated task',
                'status': self.status2,
                'executor': self.executor,
            },
        }

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
