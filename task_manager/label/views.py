from django.shortcuts import render
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    ModelFormMixin
)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Label


class LabelModelMixin(ModelFormMixin):
    model = Label
    fields = ['name']


class LabelIndexView(LoginRequiredMixin, View):
    """Label index view."""
    login_url = reverse_lazy('login')
    template = 'label/index.html'

    def get(self, request, *args, **kwargs):
        """Return label index template."""
        labels = Label.objects.all()
        return render(request, self.template, {'labels': labels})


class LabelCreateView(LoginRequiredMixin, LabelModelMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'label/create.html'


class LabelUpdateView(LoginRequiredMixin, LabelModelMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'label/update.html'


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('labels_index')
    template_name = 'label/delete.html'

    model = Label
