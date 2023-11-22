from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.utils.translation import gettext as _
# from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from .filters import TaskFilter


class UserLimitDeleteMixin(UserPassesTestMixin):
    """Limit the user ability to delete only his own tasks."""

    def test_func(self):
        """Check if the user ID match with ID extracted from URL parameters."""
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return self.request.user.pk == task.author_id

    def handle_no_permission(self):
        """Redirect to users index with flash msg."""
        msg_text = _("You don't have permition to delete the task")
        messages.error(self.request, msg_text)
        return redirect('tasks_index')


class TaskIndexView(LoginRequiredMixin, View):
    """Tasks index view."""
    login_url = 'login'
    template = 'task/index.html'

    def get(self, request, *args, **kwargs):
        """Return tasks index."""
        tasks = Task.objects.all()
        tasks_filtered = TaskFilter(
            request.GET, queryset=tasks, request=request
        )
        return render(
            request, self.template, {'filter': tasks_filtered}
        )


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Task creation view."""
    login_url = 'login'
    template_name = 'task/create.html'
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'executor',
        'labels',
    ]

    def form_valid(self, form):
        """Assign user as author to the model instance."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskReadView(LoginRequiredMixin, View):
    """Detailed task view."""
    login_url = 'login'
    template = 'task/read.html'

    def get(self, request, *args, **kwargs):
        """Return detailed task template."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        return render(request, self.template, {'task': task})


class TaskUpdateView(LoginRequiredMixin, View):
    """Task updation view."""
    login_url = 'login'
    template = 'task/update.html'

    def get(self, request, *args, **kwargs):
        """Return task update form."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(instance=task)
        return render(
            request, self.template, {'form': form, 'task_pk': task_pk}
        )

    def post(self, request, *args, **kwargs):
        """Update task on POST."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            msg_text = _('Task successfully updated')
            messages.success(request, msg_text)
            return redirect('tasks_index')
        return render(request, self.template, {'form': form})


class TaskDeleteView(LoginRequiredMixin, UserLimitDeleteMixin, View):
    """Task deletion view."""
    login_url = 'login'
    template = 'task/delete.html'

    def get(self, request, *args, **kwargs):
        """Retern task delete form."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        return render(request, self.template, {'task': task})

    def post(self, request, *args, **kwargs):
        """Delete task on POST."""
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        task.delete()
        msg_text = _('Task successfully deleted')
        messages.success(request, msg_text)
        return redirect('tasks_index')
