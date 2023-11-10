from django.db import models
from django.utils.translation import gettext_lazy as _ 

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
        'User',
        on_delete=models.PROTECT,
    )
        
    status = models.ForeignKey(
        "task_manager.status.Status",
        on_delete=models.DO_NOTHING,
    )

    executor = models.ForeignKey(
        "User",
        on_delete=models.PROTECT,
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
