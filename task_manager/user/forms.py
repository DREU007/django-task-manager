from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    """A form that creates a user, with additional fields."""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',]


class CustomUserChangeForm(PasswordChangeForm, ModelForm):
    """
    A form that changes a user data.
    """

    def __init__(self, *, user, **kwargs):
        """
        Initialize parrent classes.

        Positional args are avoided, cause user has to be specified first.
        """
        super().__init__(user, **kwargs)

    field_order = [
        'username',
        'first_name',
        'last_name',
        'old_password',
        'new_password1',
        'new_password2',
    ]

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',]
