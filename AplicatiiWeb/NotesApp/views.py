from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from NotesApp.forms import NotesForm
from NotesApp.models import Notes


# Create your views here.

class NotesView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'NotesApp/notes_index.html'
    context_object_name = 'lista_notes'

class CreateNotesView(LoginRequiredMixin, CreateView):

    model = Notes
    # fields = ['name', 'text']
    form_class = NotesForm
    template_name = 'NotesApp/notes_create.html'

    def get_form_kwargs(self):
        data = super(CreateNotesView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('NotesApp:lista_notes')

class UpdateNotesView(LoginRequiredMixin, UpdateView):
    model = Notes
    # fields = ['name', 'text']
    form_class = NotesForm
    template_name = 'NotesApp/notes_create.html'

    def get_form_kwargs(self):
        data = super(UpdateNotesView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('NotesApp:lista_notes')


def delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)

    if request.method == "POST":
        if 'confirm_delete' in request.POST:
            note.delete()
            return redirect('NotesApp:lista_notes')
        else:
            return redirect('NotesApp:lista_notes')

    return render(request, 'NotesApp/confirm_delete.html', {'note': note})

