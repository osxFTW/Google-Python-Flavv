from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class HomeView(ListView):
    template_name = 'homepage/home_index.html'
