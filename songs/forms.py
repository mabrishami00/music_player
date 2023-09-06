from django import forms


class CommentForm(forms.Form):
    body = forms.CharField(
        widget=forms.TextInput(attrs={
            "id": "text",
            "name": "text",
            "class": "sign__textarea",
            "placeholder": "Add comment",
        }
        )
    )
