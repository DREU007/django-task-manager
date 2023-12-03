from django.shortcuts import render
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    ModelFormMixin
)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect

from .models import Label


class LabelModelMixin(LoginRequiredMixin, SuccessMessageMixin, ModelFormMixin):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('labels_index')

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


class LabelCreateView(LabelModelMixin, CreateView):
    """Label create view."""
    template_name = 'label/create.html'
    success_message = _('Label is successfully created')


class LabelUpdateView(LabelModelMixin, UpdateView):
    """Label update view."""
    template_name = 'label/update.html'
    success_message = _('Label is successfully updated')


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    """Label delete view."""
    template_name = 'label/delete.html'
    success_url = reverse_lazy('labels_index')

    model = Label

    def form_valid(self, form):
        """
        Custom delete logic on POST.

        Call the delete() method on the fetched object, create
        the success message and redirect to the success URL.

        Copy behaivor of django.views.generic.edit.DeletionMixin but
        with the success_message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        msg_txt = _('Label is successfully deleted')
        messages.success(self.request, msg_txt)
        return HttpResponseRedirect(success_url)
