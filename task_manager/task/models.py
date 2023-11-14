from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse

from django.contrib.auth.models import User
from task_manager.status.models import Status


class Task(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True,
        help_text=_("Required 255 characters or fewer."),
        error_messages={
            "unique": _("Task status with such Name already exist."),
        }
    )

    description = models.TextField(
        _('description'),
        max_length=255,
        unique=False,
        help_text=_("Required 255 characters or fewer."),
        error_messages={
            "unique": _("Task status with such Name already exist."),
        }
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
    )

    # tag = models.ForeignKey(
    #     'task_manager.tag.Tag',
    #     on_delete=models.DO_NOTHING,
    # )

    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True,
    )

    def get_absolute_url(self):
        return reverse('tasks_index')

    def __str__(self):
        return f'{self.name}'
