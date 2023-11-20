from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse


class Label(models.Model):
    """Represents a label for a task in the task manager."""
    name = models.CharField(
        _('Name'),
        max_length=255,
        unique=True,
        help_text=_("Required 255 characters or fewer."),
        error_messages={
            "unique": _("Label with such name already exist."),
        }
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True,
    )

    def get_absolute_url(self):
        return reverse('labels_index')

    def __str__(self):
        return self.name
