from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Label


class LabelCRUDTest(TestCase):
    """Test label CRUD operations."""

    @classmethod
    def setUpTestData(cls):
        """Set up data for all tests."""
        user_data = {
            'username': 'tota',
            'first_name': 'Tota',
            'last_name': 'Totavich',
            'password': 'adminadmin',
        }
        cls.user = User.objects.create(**user_data)
        cls.label_data = {
            'create': {
                'name': 'bug',
            },
            'update': {
                'name': 'fix',
            }
        }

    def setUp(self):
        """Set up test enviroment."""
        self.client = Client()
        self.client.force_login(user=self.user)

    def test_create_label(self):
        """Test label creation on POST."""
        label_data = self.label_data['create']
        url = reverse('label_create')
        self.client.post(url, label_data)

        label = Label.objects.last()
        self.assertEqual(label_data['name'], label.name)

    def test_read_labels(self):
        """Test label present in label index template."""
        label_data = self.label_data['create']
        label = Label.objects.create(**label_data)
        url = reverse('labels_index')
        response = self.client.get(url)

        self.asertIn(label.name, response)

    def test_update_label(self):
        """Test label update on POST."""
        label_data = self.label_data['create']
        label = Label.objects.create(**label_data)
        url = reverse('label_update', kwargs={'pk': label.pk})

        label_updated_data = self.label_data['updated']
        self.cliet.post(url, label_updated_data)
        label_updated = Label.objects.get(pk=label.pk)
        self.assertEqual(label_updated_data['name'], label_updated.name)

    def test_delete_label(self):
        """Test label delete on POST."""
        label_data = self.label_data['create']
        label = Label.objects.create(**label_data)
        url = reverse('label_delete', kwargs={'pk': label.pk})

        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(pk=label.pk)
