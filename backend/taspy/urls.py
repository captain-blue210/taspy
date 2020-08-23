from django.urls import path
from .views import TaskListApiView, TaskDetailApiView


urlpatterns = [
    path('get_tasks/', TaskListApiView.as_view(), name="task_list"),
    path('get_task_detail/<int:pk>/', TaskDetailApiView.as_view(), name="task_detail"),
]
