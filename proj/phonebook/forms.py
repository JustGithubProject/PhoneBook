from django import forms

from .models import Person


class CreatePersonForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text="separated by newline")

    class Meta:
        model = Person
        fields = ["name", "phones"]
