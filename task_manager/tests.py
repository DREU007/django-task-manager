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
