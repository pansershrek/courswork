from django import forms
from .models import Texts


class TextForm(forms.Form):
    title = forms.CharField()
    text_value = forms.CharField()
    tags = forms.CharField()


class TitlesForm(forms.Form):
    titles_liked = forms.ModelChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Texts.objects.all(),
    )
    titles_dislike = forms.ModelChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Texts.objects.all(),
    )


class TitleForm(forms.Form):
    title = forms.CharField()
