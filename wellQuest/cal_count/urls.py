from django.urls import path
from . import views

urlpatterns = [
    path('', views.cal_count, name='cal_count'),
]