from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Status 
from .forms import StatusForm 

class StatusIndexView(LoginRequiredMixin, View):
    """Index statuses view."""
    # login_url = reverse('login')
    template = 'status/index.html'

    def get(self, request, *args, **kwargs):
        "Render statuses within status index template."""
        statuses = Status.objects.all()
        return render(request, self.template, context={"statuses": statuses})


class StatusCreateView(LoginRequiredMixin, View):
    """Create status view."""
    template = 'status/create.html'

    def get(self, request, *args, **kwargs):
        """Render create status form template."""
        form = StatusForm()
        return render(request, self.template, {"form": form})

    def post(self, request, *args, **kwargs):
        """Create status on POST with a valid data."""
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            msg_text = _('Status successfully created')
            messages.success(request, msg_text)
            return redirect('status_index')
        return render(request, self.template, {"form": form})


class StatusUpdateView(LoginRequiredMixin, View):
    """Update status view."""
    template = 'status/update.html'

    def get(self, request, *args, **kwargs):
        """Render update status form."""
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(instance=status) # StatusChangeForm ??
        return render(
            request, self.template, {'form': form, 'status_pk': status_pk}
        )

    def post(self, request, *args, **kwargs):
        """Update status on POST."""
        status_pk = kwargs.get('pk')
        status = Status.objects.get(pk=status_pk)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
           form.save()
           msg_text = _('Status successfully updated')
           messages.success(request, msg_text)
           return redirect('status_index')
        return render(
            request, self.template, {'form': form, 'status_pk': status_pk}
        )

class StatusDeleteView(LoginRequiredMixin, View):
    """Delete status view."""
    template = 'status/delete.html'

    def get(self, request, *args, **kwargs):
        """Render delete status form."""
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(request, self.template, {'status': status}) 

    def post(self, request, *args, **kwargs):
        """Delete status on POST."""
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        msg_text = _('Status successfully deleted')
        messages.success(request, msg_text)
        return redirect('status_index')
