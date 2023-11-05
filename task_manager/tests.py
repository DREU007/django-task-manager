from django.test import Client, TestCase
from django.shortcuts import reverse

import unittest
from selenium import webdriver

from django.contrib.auth.models import User
from task_manager.user.forms import CustomUserCreationForm


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


class UserCreateTest(TestCase):
    """Test user creation operations."""
    
    def setUp(self):
        """Set initial condition for each test method."""  
        self.client = Client()
        self.data = {
            'user1': {
                'username': 'tota',
                'first_name': 'Tota',
                'last_name': 'Totavich',
                'password1': 'adminadmin',
                'password2': 'adminadmin',
            },
            'user2': {
                'username': 'dada',
                'first_name': 'Dada',
                'last_name': 'Dadavich',
                'password1': 'adminadmin',
                'password2': 'adminadmin',
            },
            'wrong_user': {
                'username': '',
                'first_name': '',
                'last_name': '',
                'password1': 'a',
                'password2': 'b',
            }
        }

    def test_create_user_view(self):
        """Test user creation view."""
        url = reverse('user_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_form_valid(self):
        """Test user creation form validation with correct data."""
        user = self.data['user1']
        form = CustomUserCreationForm(user)
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid(self):
        """Test user creation form failure with wrong data."""
        user = self.data['wrong_user']
        form = CustomUserCreationForm(user)
        self.assertFalse(form.is_valid())

    def test_create_user_on_post(self):
        """Test user creation on post."""
        url = reverse('user_create')
        user = self.data['user1']
        response = self.client.post(url, user)
        new_user = User.objects.last()
        self.assertEqual(user['username'], new_user.username)
        self.assertEqual(user['first_name'], new_user.first_name)
        self.assertEqual(user['last_name'], new_user.last_name)


class UserRUDTest(TestCase):
    """Test user read, update, delete operations."""

    def setUp(self):
        """Set initial condition for each test method."""  
        self.client = Client()
        self.data = {
            'user': {
                'username': 'tota',
                'first_name': 'Tota',
                'last_name': 'Totavich',
                'password': 'adminadmin',
            },
            'user_updated': {
                'username': 'dada',
                'first_name': 'Dada',
                'last_name': 'Dadavich',
                'old_password': 'adminadmin',
                'new_password1': 'adminadmin',
                'new_password2': 'adminadmin',
            },
        }

    def test_read_user(self):
        """Test user present on view."""
        url = reverse('users_index')
        user = self.data['user']
        User.objects.create(**user)

        response = self.client.get(url)
        response_text = response.content.decode('utf-8')

        self.assertIn(user['username'], response_text) 
        self.assertIn(user['first_name'], response_text) 
        self.assertIn(user['last_name'], response_text) 

    def test_update_user(self):
        """Test user update data."""
        user = self.data['user']
        user_updated = self.data['user_updated']

        new_user = User.objects.create_user(**user)

        login_url = reverse('login')
        login_response = self.client.post(
            login_url, {
                'username': user['username'],
                'password': user['password']
            }
        )

        url = reverse('user_update', kwargs={'pk': new_user.pk})
        response = self.client.post(url, user_updated)

        updated_user = User.objects.get(pk=new_user.pk) 
        self.assertEqual(user_updated['username'], updated_user.username)
        self.assertEqual(user_updated['first_name'], updated_user.first_name)
        self.assertEqual(user_updated['last_name'], updated_user.last_name)
