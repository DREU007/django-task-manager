from django.views import View
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.utils import lazy_gettext as _


class IndexView(View):
    """Root index view."""
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CustomLoginView(SuccessMessageMixin, LoginView):
    """User login page view."""
    template_name = 'user/login.html'
    next_page = reverse_lazy('users_index')
    success_message = _("You are logged in")
