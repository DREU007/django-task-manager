from django.views import View
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):
    """Root index view."""
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CustomLoginView(SuccessMessageMixin, LoginView):
    """User login page view."""
    template_name = 'user/login.html'
    next_page = reverse_lazy('users_index')
    success_message = "Yes!" # translate
