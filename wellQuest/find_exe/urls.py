from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercises, name='exercises'),
     path('<int:active_exercises>', views.exercises, name='exercises'),
]