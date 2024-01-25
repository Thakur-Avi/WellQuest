from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def fitness_index(request):
    return render(request, 'bmi.html')