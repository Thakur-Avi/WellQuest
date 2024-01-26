
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def mental_wellness(request):
    return render(request, 'mental_health.html')