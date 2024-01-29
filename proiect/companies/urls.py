from django.urls import path

from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompanyView.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateCompanyView.as_view(), name='modificare'),
]
