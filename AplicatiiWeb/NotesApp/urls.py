from django.urls import path

from NotesApp import views

app_name = 'NotesApp'

urlpatterns = [
    path('', views.NotesView.as_view(), name='lista_notes'),
    path('adaugare/', views.CreateNotesView.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateNotesView.as_view(), name='modificare'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]