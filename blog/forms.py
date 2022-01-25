from django import forms
from .models import character

class CharacterForm (forms.ModelForm):
    character_name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))


    class Meta:
        model = character
        fields = '__all__'