from django.urls import path
from . import views

urlpatterns = [
    path('', views.mental_wellness, name='mental_wellness'),
]