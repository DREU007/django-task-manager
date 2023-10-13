from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """Extended user creation form."""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',]


class CustomUserChangeForm(UserChangeForm):
    """Altered user update form."""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password',]
