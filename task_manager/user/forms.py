from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class CustomUserCreationForm(UserCreationForm):
    """An user creation form."""

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name",)
