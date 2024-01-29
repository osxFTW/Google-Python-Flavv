from django.forms import TextInput
from django import forms

from companies.models import Companies


class LocationForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ['name', 'website', 'company_type']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name value', 'class': 'form-control'}),
            'website': TextInput(attrs={'placeholder': 'Website value', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        name_value = self.cleaned_data.get('name')
        website_value = self.cleaned_data.get('website')
        if self.pk:
            if Companies.objects.filter(name__icontains=name_value, website__icontains=website_value).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(['Numele si website-ul deja exista'])
        else:
            if Companies.objects.filter(name__icontains=name_value, website__icontains=website_value).exists():
                self._errors['name'] = self.error_class(['Numele si website-ul deja exista'])
        return self.cleaned_data