from django import forms

from .models import Answer


class QuestionForm(forms.Form):
    CHOICES = (
        ("a", "1"),
        ("b", "2"),
        ("c", "3"),
        ("d", "4"),
    )
    picked = forms.MultipleChoiceField(
        choices=CHOICES, widget=forms.CheckboxSelectMultiple()
    )


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["question", "is_correct"]

    text = forms.ModelChoiceField(queryset=Answer.objects.all())
