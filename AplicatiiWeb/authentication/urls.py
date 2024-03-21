from django.contrib import admin
from django.urls import path, include

from authentication import views

urlpatterns =[
    path('', views.auth_user_view, name="login"),
    path('signup', views.signup, name="signup"),
    path('notes/', include('NotesApp.urls'), name='notes'),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
]