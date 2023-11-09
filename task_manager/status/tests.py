from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Status


class StatusCRUDTest(TestCase):
    """Tests for status CRUD operation."""
    user_data = {
        'username': 'tota',
        'first_name': 'Tota',
        'last_name': 'Totavich',
        'password': 'adminadmin',
    }
    
    def setUp(self):
        """Set up test enviroment."""
        self.client = Client()
        self.data = {
            'create': {'name': 'Example status'},
            'update': {'name': 'Updated status'},
        }

        user = User.objects.create_user(**self.user_data)
        login_url = reverse('login')
        self.client.post(
            login_url,
            {
                'username': self.user_data['username'],
                'password': self.user_data['password']
            }
        )
        # self.assertTrue(self.request.user.is_authenticated())

    def test_status_create(self):
        """Test status creation on POST."""

        url = reverse('status_create')
        status_data = self.data['create']

        response = self.client.post(url, status_data)
        status = Status.objects.last()
        self.assertEqual(status.name, status_data['name'])

    def test_status_read(self):
        """Test a status present in index view."""
        url = reverse('status_index')
        status_data = self.data['create']
        status = Status.objects.create(**status_data)
        
        response = self.client.get(url)
        self.assertIn(status.name, response.content.decode('utf-8'))

    def test_status_update(self):
        """Test status update on POST."""
        status_data = self.data['create']
        status = Status.objects.create(**status_data)
        url = reverse('status_update', kwargs={'pk': status.pk})
        
        status_updated_data = self.data['update']
        response = self.client.post(url, status_updated_data)

        status_updated = Status.objects.get(pk=status.pk)
        self.assertEqual(status_updated_data['name'], status_updated.name)
    
    def test_status_delete(self):
        """Test status delete on POST."""
        status_data = self.data['create']
        status = Status.objects.create(**status_data)
        url = reverse('status_delete', kwargs={'pk': status.pk})

        response = self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=status.pk)    
