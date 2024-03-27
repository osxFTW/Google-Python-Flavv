from django import forms
from django.forms import TextInput, inlineformset_factory, BaseInlineFormSet, formset_factory

from quizapp.models import Questions, Answer


AnswerFormSet = inlineformset_factory(Questions, Answer, fields=('text_answer', 'is_correct'), extra=4, max_num=4)

class QuizForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ['text_quiz']
        labels = {'text_quiz': 'Quiz name'}

        widgets = {
            'text_quiz': TextInput(attrs={'placeholder': 'Quiz name', 'class': 'form-control'})
        }



    def clean(self):
        cleaned_data = super().clean()
        text_quiz_value = cleaned_data.get('text_quiz')
        if Questions.objects.filter(text_quiz__icontains=text_quiz_value).exclude(id=self.instance.id).exists():
            self.add_error('text_quiz', 'Name of quiz already exists')
        return cleaned_data

class BaseAnswerFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseAnswerFormSet, self).__init__(*args, **kwargs)
        self.queryset = self.queryset.none()  # Asigură-te că nu există niciun obiect în queryset inițial

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text_answer', 'is_correct']
        labels = {'text_answer': 'Answer', 'is_correct': 'Is Correct'}
        widgets = {
            'text_answer': forms.TextInput(attrs={'placeholder': 'Answer', 'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(),
        }


