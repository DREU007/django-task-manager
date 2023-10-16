from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . import forms


class UsersView(View):
    """Users page view."""

    def get(self, request, *args, **kwargs):
        """Return all users."""
        users = User.objects.all() 
        return render(request, 'user/index.html', {'users': users})


class UserCreateView(View):
    """User create page view."""

    def get(self, request, *args, **kwargs):
        """Return a user creation form."""
        form = forms.CustomUserCreationForm()
        return render(request, 'user/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """Create a new user."""
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_index')
        return render(request, 'user/create.html', {'form': form}) 


class UserUpdateView(View):
    """User update page view."""

    def get(self, request, *args, **kwargs):
        """Return a user data filled form."""
        user_id = kwargs.get('pk')
        user = get_object_or_404(User, pk=user_id)
        form = forms.CustomUserChangeForm(user=user, instance=user)
        return render(
            request,
            'user/update.html',
            {'form': form, 'user_id': user_id}
        )

    def post(self, request, *args, **kwargs):
        """Update a user data."""
        user_id = kwargs.get('pk')
        user = get_object_or_404(User, pk=user_id)
        form = forms.CustomUserChangeForm(user=user, data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_index')
        return render(
            request,
            'user/update.html',
            {'form': form, 'user_id': user_id}
        )


class UserDeleteView(View):
    """User delete page view."""

    def get(self, request, *args, **kwargs):
        """Render delete user template."""
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        return render(request, 'user/delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        """Delete user."""
        # flash_msg
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        user.delete()
        return redirect('users_index')


class UserLoginView(View):
    """User login page view."""

    def get(self, request, *args, **kwargs):
        """Render user login template."""
        form = AuthenticationForm()
        return render(request, 'user/login.html', {"form": form})

    def post(self, request, *args, **kwargs):
        """Log in a user."""
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users_index')
        return render(request, 'user/login.html', {"form": form})

class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        """Log out a user."""
        logout(request)
        return redirect('index')
