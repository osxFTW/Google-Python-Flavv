from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from companies.forms import LocationForm
from companies.models import Companies


# Create your views here.

class CompanyView(ListView):
    model = Companies
    context_object_name = 'companies'
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

class UpdateCompanyView(UpdateView):
    model = Companies
    form_class = LocationForm
    template_name = 'companies/location_form.html'

    def get_form_kwargs(self):
        data = super(UpdateCompanyView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('companies:lista_companii')

def deactivate_location(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:lista_companii')


def activate_location(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:lista_companii')

def delete(request, pk):
    company = get_object_or_404(Companies, pk=pk)

    if request.method == "POST":
        if 'confirm_delete' in request.POST:
            company.delete()
            return redirect('companies:lista_companii')
        else:
            return redirect('companies:lista_companii')

    return render(request, 'companies/confirm_delete.html', {'company': company})