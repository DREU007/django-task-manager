from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all() 
        return render(request, 'user/index.html', {'users': users})
