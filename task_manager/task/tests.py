from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from task_manager.status.models import Status
from task_manager.label.models import Label
from .models import Task
from .filters import TaskFilter


class TaskCRUDTest(TestCase):
    """Tests for task CRUD operation."""

    @classmethod
    def setUpTestData(cls):
        """
        Set up data for tests.

        Set up class attributes and create objects:
        author, executor as User objects
        status_original, status_updated as Status objects

        data - a data for Task object creation
        """
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

        status_data = {
            'create': {'name': 'Example status'},
            'update': {'name': 'Updated status'},
        }
        cls.status_original = Status.objects.create(**status_data['create'])
        cls.status_updated = Status.objects.create(**status_data['update'])

        cls.orm_user_create_data = {
            'name': 'Example task',
            'description': 'This is example task',
            'status': cls.status_original,
            'executor': cls.author,
            'author': cls.author,
        }
        cls.data = {
            'create': {
                'name': 'Example task',
                'description': 'This is example task',
                'status': cls.status_original.pk,
                'executor': cls.author.pk,
            },
            'update': {
                'name': 'Updated task',
                'description': 'This is updated task',
                'status': cls.status_updated.pk,
                'executor': cls.executor.pk,
            },
        }

    def setUp(self):
        """Set up test enviroment and keep user logged in."""
        self.client = Client()
        self.client.force_login(
            user=self.author
        )

    def test_create_task(self):
        """Test task creation in db on POST."""
        url = reverse('task_create')
        task_data = self.data['create']
        self.client.post(url, task_data)

        task = Task.objects.last()
        self.assertEqual(task.name, task_data['name'])
        self.assertEqual(task.description, task_data['description'])
        self.assertEqual(task.status_id, self.status_original.pk)

    def test_read_tasks_index(self):
        """Test tasks index reading."""
        url = reverse('tasks_index')
        task_data = self.orm_user_create_data
        task = Task.objects.create(**task_data)

        response = self.client.get(url)
        content = response.content.decode('utf-8')
        self.assertIn(task.name, content)
        self.assertIn(task.status.name, content)

    def test_update_task(self):
        """Test task updation on POST."""
        task_data = self.orm_user_create_data
        task = Task.objects.create(**task_data)
        url = reverse('task_update', kwargs={'pk': task.pk})

        task_updated_data = self.data['update']
        self.client.post(url, task_updated_data)

        task_updated = Task.objects.get(pk=task.pk)
        self.assertEqual(task_updated.name, task_updated_data['name'])
        self.assertEqual(
            task_updated.description, task_updated_data['description']
        )

    def test_delete_task(self):
        """Test task deletion on POST."""
        task_data = self.orm_user_create_data
        task = Task.objects.create(**task_data)
        url = reverse('task_delete', kwargs={'pk': task.pk})

        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(pk=task.pk)


class TaskFilterTest(TestCase):
    """Test queryset task filter with fixtures in database."""
    fixtures = ['filter_fixtures.json']

    def test_filter_status(self):
        """Test queryset status filter."""
        status = Status.objects.get(name='Example status')
        qs_filter = TaskFilter(
            data={'status': status.pk}, queryset=Task.objects.all()
        )
        self.assertEqual(
            list(qs_filter.qs),
            list(Task.objects.filter(status=status.pk)),
        )

    def test_filter_label(self):
        """Test queryset label filter."""
        label = Label.objects.get(name='fix')
        qs_filter = TaskFilter(
            data={'labels': label.pk}, queryset=Task.objects.all()
        )
        self.assertEqual(
            list(qs_filter.qs), list(Task.objects.filter(labels=label.pk))
        )

    def test_filter_author(self):
        """Test queryset author filter."""
        author = User.objects.get(username="tota")
        qs_filter = TaskFilter(
            data={'author': author.pk}, queryset=Task.objects.all()
        )
        self.assertEqual(
            list(qs_filter.qs), list(Task.objects.filter(author=author.pk))
        )
