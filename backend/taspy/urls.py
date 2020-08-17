from django.urls import path
from .views import PersonListApiView


urlpatterns = [
    path('get_person/', PersonListApiView.as_view()),
]
