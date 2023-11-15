from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.task.models import Task


class Label(models.Model):
    """Represents a label for a task in the task manager."""
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True,
        help_text=_("Required 255 characters or fewer."),
        error_messages={
            "unique": _("Task status with such Name already exist."),
        }
    )
    task = models.ManyToManyField(
       Task,
       on_delete=models.PROTECT,
    )
