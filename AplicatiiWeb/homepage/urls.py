from django.urls import path

from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.HomeView, name='home'),

]