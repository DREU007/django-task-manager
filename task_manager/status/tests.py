from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist

from . import models


class StatusCRUDTest(TestCase):
    """Tests for status CRUD operation."""
    
    def setUp(self):
        """Set up test enviroment."""
        self.client = Client()
        self.data = {
            'create': 'Example status',
            'update': 'Updated status',
        }

    def test_status_create(self):
        """Test status creation on POST."""
        url = reverse('status_create')
        status_data = self.data['create']
        response = self.client.post(url, status_data)

        status = Status.objects.last()
        self.assertEqual(status.name, status_data) 

    def test_status_read(self):
        """Test a status present in index view."""
        url = reverse('status_index')
        status_data = self.data['create']
        status = Status.objects.create(status_data)
        
        response = self.client.get(url)
        self.assertIn(status.name, response.content)

    def test_status_update(self):
        """Test status update on POST."""
        status_data = self.data['create']
        status = Status.objects.create(status_data)
        url = reverse('status_update', kwargs={'pk': status_data.pk})
        
        status_updated_data = self.data['update']
        response = self.client.post(url, status_updated_data)

        status_updated = Status.objects.get(pk=status.pk)
        self.assertEqual(updated_status, status_updated.pk) 
    
    def test_status_delete(self):
        """Test status delete on POST."""
        status_data = self.data['create']
        url = reverse('status_delete', kwargs={'pk': status_data.pk})
        status = Status.objects.create(status_data)

        response = self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=status.pk)    
