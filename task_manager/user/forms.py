from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    """A form that creates a user, with additional fields."""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',]


class CustomUserChangeForm(CustomUserCreationForm):
    """A form that changes a user data."""

    def clean_username(self):
        """
        Reject change of username if it is in use by other User.

        Based on django.contrib.auth.forms.UserCreationForm.
        """
        username = self.cleaned_data.get("username")
        instance = self.instance

        other_instance = self._meta.model.objects.exclude(
            pk=instance.pk
        ).filter(username__iexact=username)

        if other_instance.exists():
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username

    field_order = [
        'username',
        'first_name',
        'last_name',
    ]
