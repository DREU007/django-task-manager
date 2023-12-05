from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse

from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label


class Task(models.Model):
    """Represents a task in the task manager."""
    name = models.CharField(
        _('Name'),
        max_length=255,
        unique=True,
        help_text=_("Required 255 characters or fewer."),
        error_messages={
            "unique": _("Task with such name already exist."),
        }
    )

    description = models.TextField(
        _('Description'),
        max_length=255,
        unique=False,
        blank=True,
        null=True,
        help_text=_("Required 255 characters or fewer."),
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author'),
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        blank=True,
        null=True,
        verbose_name=_('Executor'),
    )

    labels = models.ManyToManyField(
        Label,
        blank=True,
        verbose_name=_('Labels'),
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
        return reverse('tasks_index')

    def __str__(self):
        return f'{self.name}'
