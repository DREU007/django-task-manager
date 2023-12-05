import django_filters
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label


class TaskFilter(django_filters.FilterSet):
    """Set of filters for the Task model."""
    name = django_filters.CharFilter(
        label=_('Name'),
        label_suffix="",
        field_name="name",
        lookup_expr='icontains',
    )
    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        label_suffix="",
        queryset=Status.objects.all(),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Executor'),
        label_suffix="",
        queryset=User.objects.all(),
    )
    author = django_filters.ModelChoiceFilter(
        label=_('Author'),
        label_suffix="",
        queryset=User.objects.all(),
    )
    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        label_suffix="", queryset=Label.objects.all(),
    )
    is_author = django_filters.BooleanFilter(
        label=_('Only my tasks'),
        label_suffix="",
        method='filter_is_author',
        widget=forms.CheckboxInput(),
    )

    is_executor = django_filters.BooleanFilter(
        label=_('Only tasks for me'),
        label_suffix="",
        method='filter_is_executor',
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = Task
        fields = [
            'name',
            'status',
            'executor',
            'author',
        ]

    def filter_is_author(self, queryset, name, value):
        """Return queryset of the user created tasks."""
        if value:
            lookup = 'author__id'
            return queryset.filter(**{lookup: self.request.user.id})
        return queryset

    def filter_is_executor(self, queryset, name, value):
        """Return queryset of deligated to the user tasks."""
        if value:
            lookup = 'executor__id'
            return queryset.filter(**{lookup: self.request.user.id})
        return queryset
