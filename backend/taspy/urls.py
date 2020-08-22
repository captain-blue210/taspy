from django.urls import path
from .views import TaskListApiView


urlpatterns = [
    path('get_task/', TaskListApiView.as_view()),
]
