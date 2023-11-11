from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from .models import Task
from .forms import TaskForm


class TaskIndexView(LoginRequiredMixin, View):
    """Tasks index view."""
    login_url = 'login'
    template = 'task/index.html'

    def get(self, request, *args, **kwargs):
        """Return tasks index."""
        tasks = Task.objects.all()
        return render(request, template, {'tasks': tasks})


class TaskCreateView(LoginRequiredMixin, View):
    """Task creation view."""
    login_url = 'login'
    template = 'task/create.html'

    def get(self, request, *args, **kwargs):
        """Return task creation form."""
        form = TaskForm()
        return render(request, template, {'form': form})

    def post(self, request, *args, **kwargs):
        """Create task on POST."""
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            msg_text = _('Task is successefully created')
            messages.success(request, msg_text)
            return redirect('tasks_index')
        msg_text = _('Somthing wrong') # TODO:
        messages.error(request, msg_text)
        return render(request, template, {'form': form})


class TaskUpdateView(LoginRequiredMixin, View): 
    """Task updation view."""
    login_url = 'login'
    template = 'task/update.html'

    def get(self, request, *args, **kwargs):
        """Return task update form."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(Task, instance=task)
        return render(request, template, {'form': form})

    def post(self, request, *args, **kwargs):
        """Update task on POST."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(instance=task)
        if form.is_valid():
            form.save()
            msg_text = _('Successfully updated task')
            messages.success(request, msg_text)
            return redirect('tasks_index')
        msg_text = _('Somthing wrong') # TODO:
        messages.error(request, msg_text)
        return render(request, template, {'form': form})
