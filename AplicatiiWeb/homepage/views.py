from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def HomeView(request):
    template_name = 'homepage/home_index.html'

    return render(request, 'homepage/home_index.html')
