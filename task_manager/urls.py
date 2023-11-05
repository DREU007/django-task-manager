"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include, reverse_lazy
from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.IndexView.as_view(), name='index'),
    path(
        'login/',
        views.CustomLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(next_page=reverse_lazy('users_index')),
        name='logout'
    ),
    path('users/', include('task_manager.user.urls')),
    path('admin/', admin.site.urls),
]
