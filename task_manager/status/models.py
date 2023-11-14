from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    """Task status one-to-many tasks."""
    name = models.CharField(
        _("name"),
        max_length=255,
        unique=True,
        help_text=_("Required 255 characters or fewer."),
        error_messages={
            "unique": _("Task status with such Name already exist."),
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

    def __str__(self):
        return self.name
