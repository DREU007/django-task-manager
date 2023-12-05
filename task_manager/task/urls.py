from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskIndexView.as_view(), name='tasks_index'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path(
        '<int:pk>/',
        views.TaskReadView.as_view(),
        name='task_read'
    ),
    path(
        '<int:pk>/update/',
        views.TaskUpdateView.as_view(),
        name='task_update'
    ),
    path(
        '<int:pk>/delete/',
        views.TaskDeleteView.as_view(),
        name='task_delete'
    ),
]
