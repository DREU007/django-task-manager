import django_filters
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _
from task_manager.label.models import Label


class TaskFilter(django_filters.FilterSet):
    """Set of filters for the Task model."""
    name = django_filters.CharFilter(
        label=_('Name'),
        field_name="name",
        lookup_expr='icontains'
    )
    labels = django_filters.ModelChoiceFilter(
        # label=_('Label'),
        queryset=Label.objects.all()
    )
    is_author = django_filters.BooleanFilter(
        label=_('Only my tasks'),
        method='filter_is_author',
        widget=forms.CheckboxInput()
    )

    is_executor = django_filters.BooleanFilter(
        label=_('Only tasks for me'),
        method='filter_is_executor',
        widget=forms.CheckboxInput()
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
