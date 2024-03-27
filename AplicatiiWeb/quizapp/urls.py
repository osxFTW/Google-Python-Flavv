from django.urls import path, include

from quizapp import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.index),
    path('list_quiz/', views.QuizView.as_view(), name='list_quiz'),
    path('add_quiz/', views.CreateQuizView.as_view(), name='add_quiz'),
    path('start_quiz/', views.quiz_view, name='start_quiz'),
    path('<int:pk>/modify/', views.UpdateQuizView.as_view(), name='modify'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
