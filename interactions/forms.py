from django import forms

class AddPlaylistForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
