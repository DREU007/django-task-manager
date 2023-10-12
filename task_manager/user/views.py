from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import forms

class UsersView(View):
    """Users page view."""

    def get(self, request, *args, **kwargs):
        """Return all users."""
        users = User.objects.all() 
        return render(request, 'user/index.html', {'users': users})


class UserCreateView(View):
    """User create view."""

    def get(self, request, *args, **kwargs):
        """Return registration form."""
        form = UserCreationForm()
        return render(request, 'user/form.html', {'form': form})
