from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from companies.models import Companies


# Create your views here.

class CompanyView(ListView):
    model = Companies
    template_name = 'companies/location_index.html'

class CreateCompanyView(CreateView):
    model = Companies
    fields = ['name', 'website', 'company_type', 'location']
    template_name = 'companies/location_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')

class UpdateCompanyView(UpdateView):
    model = Companies
    fields = ['name', 'website', 'company_type', 'location']
    template_name = 'companies/location_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')