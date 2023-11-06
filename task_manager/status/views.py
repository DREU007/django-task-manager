from django.shortcuts import render, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


class StatusIndexView(LoginRequiredMixin, View):
    """Index statuses view."""
    # login_url = reverse('login')
    template = 'status/index.html'

    def get(self):
        return render(request, template)
