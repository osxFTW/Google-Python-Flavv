from django import forms
from django.forms import TextInput

from NotesApp.models import Notes


class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['name', 'text']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Note name', 'class': 'form-control'}),
            'text': TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(NotesForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        name_value = self.cleaned_data.get('name')
        text_value = self.cleaned_data.get('text')
        if self.pk:
            if Notes.objects.filter(name__icontains=name_value).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(['Name already exists'])
        else:
            if Notes.objects.filter(name__icontains=name_value).exists():
                self._errors['name'] = self.error_class(['Name already exists'])
        return self.cleaned_data