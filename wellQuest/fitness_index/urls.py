from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness_index, name='fitness_index'),
]