from django.test import Client, TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):
    """Test registration page."""
    
    def setUp(self):
        """Set initial condition for each test method."""  
        self.client = Client()

    def test_home_page_view(self):
        """Test home page 200 status."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class UserCRUDTest(TestCase):
    """Test pages for user CRUD operations."""
    
    def setUp(self):
        """Set initial condition for each test method."""  
        client = Client()
        data = {
                'username': 'tota',
                'first_name': 'Tota',
                'last_name': 'Totavich',
                'password1': 'adminadmin',
                'password2': data['password1'],
        }

    def test_create_user_view(self):
        """Test user creation view."""
        url = reverse('user_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_form(self):
        k1
