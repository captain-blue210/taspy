from django.shortcuts import render
from django.views.generic import ListView

from .models import Task

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .renderers import TaskJSONRenderer, TaskListJSONRenderer
from .serializers import TaskSerializer

# Create your views here.

class TaskListApiView(ListAPIView):
    model = Task # モデルを指定
    queryset = Task.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (TaskListJSONRenderer, ) # Rendererを指定
    serializer_class = TaskSerializer # Serializerを指定

class TaskDetailApiView(RetrieveAPIView):
    model = Task
    queryset = Task.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (TaskJSONRenderer, ) # Rendererを指定
    serializer_class = TaskSerializer # Serializerを指定
