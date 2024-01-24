from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')