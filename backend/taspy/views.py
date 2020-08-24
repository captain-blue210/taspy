from django.shortcuts import render

from .models import Task

from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .renderers import TaskJSONRenderer
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (TaskJSONRenderer, )
    serializer_class = TaskSerializer
