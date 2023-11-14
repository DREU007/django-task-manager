from django.forms import ModelForm
from . import models


class StatusForm(ModelForm):
    class Meta:
        model = models.Status
        fields = ['name']
